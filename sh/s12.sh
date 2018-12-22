#!/bin/bash

echo "$0 $@ $#"
say_hello() {
	echo "Hello $0 $@ by $2!! ($#)"
}
say_hello "Jade" "Jeon"


