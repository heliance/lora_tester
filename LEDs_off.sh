#!/bin/bash

LEDS=$(ps -ax | grep leds.py | sed -n '2p' | awk '{print $1}' | wc -l)
if [ "$LEDS" -lt "1" ]
        then
        echo 'No active LEDS process detected. Exiting in 3 seconds...'
        sleep 3
        exit 0
else
        LEDS=$(ps -ax | grep leds.py | sed -n '2p' | awk '{print $1}')
        kill -int $LEDS
        echo "The LEDS process with pid" $LEDS "has been killed.
        Exiting in 3 seconds..."
        sleep 3
fi
        exit 0
