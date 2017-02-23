--DESCRIPTION--

Test six macros

--GIVEN--

¼ + ¾ + ⅓ + ⅔ + ½

$this→foo()

(new Thing)→var

["foo" ⇒ "bar"]

1 ⇔ 2

"1" ≈ true

0 ≡ false

1 ≤ 2

2 ≥ 1

💩 InvalidArgumentException

--EXPECT--

(1/4) + (3/4) + (1/3) + (2/3) + (1/2)

$this->foo()

(new Thing)->var

["foo" => "bar"]

1 <=> 2

"1" == true

0 === false

1 <= 2

2 >= 1

throw new InvalidArgumentException
