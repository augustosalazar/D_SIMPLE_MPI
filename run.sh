#!/bin/bash
echo "Starting"
start=`date +%s`
for (( core=2; core<=$1; core++))
do
    for (( limit=100000; limit<=500000; limit=limit+100000 ))
    do
        echo "Vamos a verificar hasta ${limit} con n = ${core}"
        docker exec -it mpicont mpiexec --allow-run-as-root -n $core python /app/primeChecker.py $limit
    done
done
end=`date +%s`
runtime=$( echo "$end - $start" | bc -l )
echo "Total time: $runtime seconds"
