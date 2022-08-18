#!/bin/bash

COMMAND="lpr -P Qubit -o page-ranges=2 -o media=Custom.62x29mm ticket.pdf && sleep 1 && rm -rf ticket.pdf"
 
if [ -z "$(which inotifywait)" ]; then
    echo "inotifywait not installed."
    echo "In most distros, it is available in the inotify-tools package."
    exit 1
fi
 
counter=0;
 
function execute() {
    counter=$((counter+1))
    echo "Detected change n. $counter" 
    eval "${COMMAND}"
}
 
inotifywait --recursive --monitor --format "%e %w%f" \
--event move,create ./ \
| while read changed; do
    echo $changed
    execute "${COMMAND}"
done
