<?php

namespace Yay\DSL\Expanders;

use Yay\Engine;
use Yay\Token;
use Yay\TokenStream;

function six_arrow(TokenStream $stream, Engine $engine): TokenStream
{
    $current = $stream->current();

    $parts = explode("→", $current);
    $tokens = [];

    foreach ($parts as $i => $part) {
        if ($i > 0) {
            array_push($tokens, new Token(T_OBJECT_OPERATOR, "->"));
        }

        array_push($tokens, new Token(T_VARIABLE, $part));
    }

    return TokenStream::fromSequence(
        ...$tokens
    );
}
