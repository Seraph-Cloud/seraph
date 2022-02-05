<?php
// parser for simple PHP arrays
class Parser {
  private static $CONSTANTS = array(
    "null" => null,
    "true" => true,
    "false" => false
  );

  private $tokens;

  public function __construct(Tokens $tokens) {
    $this->tokens = $tokens;
  }

  public function parseValue () {
    if ($this->tokens->doesMatch(T_CONSTANT_ENCAPSED_STRING)) {
      // strings
      $token = $this->tokens->pop();
      return stripslashes(substr($token[1], 1, -1));
    }

    if ($this->tokens->doesMatch(T_STRING)) {
      // built-in string literals: null, false, true
      $token = $this->tokens->pop();
      $value = strtolower($token[1]);
      if (array_key_exists($value, self::$CONSTANTS)) {
        return self::$CONSTANTS[$value];
      }
      throw new Exception("unexpected string literal " . $token[1]);
    }

    // the rest...
    // we expect a number here
    $uminus = 1;

    if ($this->tokens->doesMatch("-")) {
      // unary minus
      $this->tokens->forceMatch("-");
      $uminus = -1;
    }

    if ($this->tokens->doesMatch(T_LNUMBER)) {
      // long number
      $value = $this->tokens->pop();
      return $uminus * (int) $value[1];
    }
    if ($this->tokens->doesMatch(T_DNUMBER)) {
      // double number
      $value = $this->tokens->pop();
      return $uminus * (double) $value[1];
    }

    throw new Exception("unexpected value token");
  }

  public function parseArray () {
    $found = 0;
    $result = array();

    $this->tokens->forceMatch(T_ARRAY);
    $this->tokens->forceMatch("(");

    while (true) {
      if ($this->tokens->doesMatch(")")) {
        // reached the end of the array
        $this->tokens->forceMatch(")");
        break;
      }

      if ($found > 0) {
        // we must see a comma following the first element
        $this->tokens->forceMatch(",");
      }

      if ($this->tokens->doesMatch(T_ARRAY)) {
        // nested array
        $result[] = $this->parseArray();
      }
      else if ($this->tokens->doesMatch(T_CONSTANT_ENCAPSED_STRING)) {
        // string
        $string = $this->parseValue();
        if ($this->tokens->doesMatch(T_DOUBLE_ARROW)) {
          // array key (key => value)
          $this->tokens->pop();
          $result[$string] = $this->parseValue();
        }
        else {
          // simple string
          $result[] = $string;
        }
      }
      else {
        $result[] = $this->parseValue();
      }

      ++$found;
    }
    return $result;
  }
}
// class to manage tokens
class Tokens {
  private $tokens;

  public function __construct ($code) {
    // construct PHP code from string and tokenize it
    $tokens = token_get_all("<?php " . $code);
    // kick out whitespace tokens
    $this->tokens = array_filter($tokens, function ($token) {
      return (! is_array($token) || $token[0] !== T_WHITESPACE);
    });
    // remove start token (<?php)
    $this->pop();
  }

  public function done () {
    return count($this->tokens) === 0;
  }

  public function pop () {
    // consume the token and return it
    if ($this->done()) {
      throw new Exception("already at end of tokens!");
    }
    return array_shift($this->tokens);
  }

  public function peek () {
    // return next token, don't consume it
    if ($this->done()) {
      throw new Exception("already at end of tokens!");
    }
    return $this->tokens[0];
  }

  public function doesMatch ($what) {
    $token = $this->peek();

    if (is_string($what) && ! is_array($token) && $token === $what) {
      return true;
    }
    if (is_int($what) && is_array($token) && $token[0] === $what) {
      return true;
    }
    return false;
  }

  public function forceMatch ($what) {
    if (! $this->doesMatch($what)) {
      if (is_int($what)) {
        throw new Exception("unexpected token - expecting " . token_name($what));
      }
      throw new Exception("unexpected token - expecting " . $what);
    }
    // consume the token
    $this->pop();
  }
}

// here's our test string (with intentionally wild usage of whitespace)
$string = " array (\"test\" => \"someValue\",
  array\n('aaa', 'bbb', 'ccc', array('ddd')),
array('AAA', 'BBB','CCC','DDD', null,1, 2, 3,-4, -42.99, -4e32, true, false))";

$tokens = new Tokens($string);
$parser = new Parser($tokens);
$result = $parser->parseArray();

// check if the parser matched the whole string or if there's something left at the end
if (! $tokens->done()) {
  throw new Exception("still tokens left after parsing");
}

var_dump("RESULT: ", $result);
?>
