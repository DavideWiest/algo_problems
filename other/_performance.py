from tqdm import tqdm
import time
import numpy as np
from matplotlib import pyplot as plt

timeUnits_tMul = {
    "ns": 1_000_000,
    "ms": 1_000,
    "s": 1,
    "m": 60,
    "h": 3600
}

# use perf_counter_ns ?

def compare_speed(fns, input_args_list, print_inputs=False, print_outputs=True, timeUnit="ms", filterByOutputLambda=None, inputAsKeyLambda=None, print_performances=True, output_timeUnit="ms"):
    if filterByOutputLambda == None: filterByOutputLambda = lambda x: True
    if inputAsKeyLambda == None: inputAsKeyLambda = lambda x: x[0] \
        if (isinstance(input_args_list[0][0], int) or isinstance(input_args_list[0][0], float)) and len(input_args_list[0]) == 1 else tuple(x)
    
    output_strings = []
    assert timeUnit in timeUnits_tMul
    tMul = timeUnits_tMul[timeUnit]
    output_tMul = timeUnits_tMul[output_timeUnit]
    
    avgTimes = [[0, 1] for i in range(len(fns))]

    input_time_dict = {fnIndex: {} for fnIndex in range(len(fns))}

    for i, inputs in enumerate(tqdm(input_args_list)):
        perfs = {}
        for fnIndex, fn in enumerate(fns):
            t0 = time.perf_counter()
            output = fn(*inputs)
            tDiff = time.perf_counter() - t0
            avgTimes[fnIndex] = [avgTimes[fnIndex][0]+tDiff*avgTimes[fnIndex][1], avgTimes[fnIndex][1]+1]
            input_time_dict[fnIndex][inputAsKeyLambda(inputs)] = tDiff*output_tMul

            if filterByOutputLambda(output) == False: continue
            
            perfs[fnIndex] = f"{fn.__name__}"
            perfs[fnIndex] += f"({', '.join([str(input) for input in inputs])})" if print_inputs else "" 
            perfs[fnIndex] +=  f" = {output}" if print_outputs else ""
            perfs[fnIndex] += f" in {tDiff*tMul:.3f}{timeUnit}"
        
        # use variable output of last iteration for checking
        if filterByOutputLambda(output) == True:
            output_strings.append(f"{i} - " + " | ".join(perfs.values()))

    if print_performances:
        print("\n".join(output_strings))
        print("\n", " | ".join(f"{fns[i].__name__}: {avgTimes[i][0]:.3f}{timeUnit}" for i in range(len(fns))))

    return input_time_dict

colorByIndex = ["g", "r", "m", "c"]

def abline(slope, intercept, color, label):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--', c=color, label=label)

def visualize_speed(fns, input_time_dict, pltShow=True):

    for fnIndex in input_time_dict:
        fnName = fns[fnIndex]
        color = colorByIndex[fnIndex]
        keys = list(input_time_dict[fnIndex].keys())
        values = list(input_time_dict[fnIndex].values())
        plt.scatter(keys, values, c=color)
        out = np.polyfit(keys, values, 1)
        slope, intercept = out[0], out[1]
    
        abline(slope, intercept, color, fnName)

    if pltShow:
        plt.show()