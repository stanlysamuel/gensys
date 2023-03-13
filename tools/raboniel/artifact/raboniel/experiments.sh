# Running Example
echo "Running Example"
echo "./raboniel --spec examples/example1/counter.tsl"
time ./raboniel --spec examples/example1/counter.tsl

# Counter experiments

echo "Counter experiments"
echo "./raboniel --spec examples/counter/counter_c1_100_5.tsl"
time ./raboniel --spec examples/counter/counter_c1_100_5.tsl
echo "./raboniel --spec examples/counter/counter_c1_100_5.tsl"
time ./raboniel --spec examples/counter/counter_c2_100_5.tsl
echo "./raboniel --spec examples/counter/counter_c1_100_5.tsl"
time ./raboniel --spec examples/counter/counter_c2_100000_50.tsl
echo "./raboniel --spec examples/counter/counter_c1_100_5.tsl"
time ./raboniel --spec examples/counter/counter_c3_100_5.tsl
echo "./raboniel --spec examples/counter/counter_c1_100_5.tsl"
time ./raboniel --spec examples/counter/counter_c3_100000_50.tsl
echo "./raboniel --spec examples/counter/counter_c1_100_5.tsl"
time ./raboniel --spec examples/counter/counter_c1_110_100.tsl
echo "./raboniel --spec examples/counter/counter_c1_100_5.tsl"
time ./raboniel --spec examples/counter/counter_c2_100_60.tsl

# Elevator experiments

echo "Elevator experiments"
echo "./raboniel --spec examples/elevator_simple/elevator3.tsl"
time ./raboniel --spec examples/elevator_simple/elevator3.tsl
echo "./raboniel --spec examples/elevator_simple/elevator4.tsl"
time ./raboniel --spec examples/elevator_simple/elevator4.tsl
echo "./raboniel --spec examples/elevator_simple/elevator5.tsl"
time ./raboniel --spec examples/elevator_simple/elevator5.tsl
# echo "./raboniel --spec examples/elevator_simple/elevator8.tsl"
# time ./raboniel --spec examples/elevator_simple/elevator8.tsl
# echo "./raboniel --spec examples/elevator_simple/elevator10.tsl"
# time ./raboniel --spec examples/elevator_simple/elevator10.tsl
echo "./raboniel --spec examples/elevator_signal/elevator_signal3.tsl"
time ./raboniel --spec examples/elevator_signal/elevator_signal3.tsl
# echo "./raboniel --spec examples/elevator_signal/elevator_signal4.tsl"
# time ./raboniel --spec examples/elevator_signal/elevator_signal4.tsl
# echo "./raboniel --spec examples/elevator_signal/elevator_signal5.tsl"
# time ./raboniel --spec examples/elevator_signal/elevator_signal5.tsl

# Sorting experiments

echo "Sorting experiments"
echo "./raboniel --spec examples/sorting/sort3.tsl"
time ./raboniel --spec examples/sorting/sort3.tsl
# echo "./raboniel --spec examples/sorting/sort4.tsl"
# time ./raboniel --spec examples/sorting/sort4.tsl
# echo "./raboniel --spec examples/sorting/sort5.tsl"
# time ./raboniel --spec examples/sorting/sort5.tsl

# Watertanks experiments
echo "Watertanks experiments"
echo "./raboniel --spec examples/watertanks/watertanks_double_safety.tsl"
time ./raboniel --spec examples/watertanks/watertanks_double_safety.tsl
echo "./raboniel --spec examples/watertanks/watertank_single_liveness.tsl"
time ./raboniel --spec examples/watertanks/watertank_single_liveness.tsl

# Obstacle avoidance experiments
echo "Obstacle avoidance experiments"
echo "./raboniel --spec examples/obstacle/static_obstacle_1.tsl"
time ./raboniel --spec examples/obstacle/static_obstacle_1.tsl
echo "./raboniel --spec examples/obstacle/static_obstacle_2.tsl --noStateExpansion"
time ./raboniel --spec examples/obstacle/static_obstacle_2.tsl --noStateExpansion
echo "./raboniel --spec examples/obstacle/dynamic_obstacle_1.tsl"
time ./raboniel --spec examples/obstacle/dynamic_obstacle_1.tsl
echo "./raboniel --spec examples/obstacle/dynamic_obstacle_2.tsl"
time ./raboniel --spec examples/obstacle/dynamic_obstacle_2.tsl

# TSL experiments
# based on
# B. Finkbeiner, F. Klein, R. Piskac, and M. Santolucito, “Temporal stream
# logic: Synthesis beyond the bools” CAV 2019
echo "TSL experiments"
# echo "./raboniel --spec examples/tsl/TwoCountersInRange.tsl --noStateExpansion"
# time ./raboniel --spec examples/tsl/TwoCountersInRange.tsl --noStateExpansion
echo "./raboniel --spec examples/tsl/OneCounterGui.tsl"
time ./raboniel --spec examples/tsl/OneCounterGui.tsl

# Infinite grid worlds 
# based on
# D. Neider and U. Topcu, “An automaton learning approach to solving
# safety games over infinite graphs” TACAS 2016
echo "Infinite grid worlds"
echo "./raboniel --spec examples/infiniteGridWorlds/box.tsl"
time ./raboniel --spec examples/infiniteGridWorlds/box.tsl
echo "./raboniel --spec examples/infiniteGridWorlds/box_limited.tsl"
time ./raboniel --spec examples/infiniteGridWorlds/box_limited.tsl
echo "./raboniel --spec examples/infiniteGridWorlds/diagonal.tsl"
time ./raboniel --spec examples/infiniteGridWorlds/diagonal.tsl
echo "./raboniel --spec examples/infiniteGridWorlds/evasion.tsl"
time ./raboniel --spec examples/infiniteGridWorlds/evasion.tsl
# echo "./raboniel --spec examples/infiniteGridWorlds/follow.tsl"
# time ./raboniel --spec examples/infiniteGridWorlds/follow.tsl # >900s
echo "./raboniel --spec examples/infiniteGridWorlds/solitary_box.tsl"
time ./raboniel --spec examples/infiniteGridWorlds/solitary_box.tsl
# echo "./raboniel --spec examples/infiniteGridWorlds/square.tsl"
# time ./raboniel --spec examples/infiniteGridWorlds/square.tsl
