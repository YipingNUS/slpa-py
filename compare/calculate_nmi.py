output_file_names = ["SLPAw_network_50000_5_run1_r0.15_v3_T100.icpm", "SLPAw_network_50000_8_run1_r0.15_v3_T100.icpm", "SLPAw_network_50000_10_run1_r0.15_v3_T100.icpm", "SLPAw_network_50000_13_run1_r0.15_v3_T100.icpm", "SLPAw_network_50000_15_run1_r0.15_v3_T100.icpm", "SLPAw_network_50000_18_run1_r0.15_v3_T100.icpm", "SLPAw_network_50000_20_run1_r0.15_v3_T100.icpm"]
first_level_file_names = ["community_first_level_50000_5.out", "community_first_level_50000_8.out", "community_first_level_50000_10.out", "community_first_level_50000_13.out", "community_first_level_50000_15.out", "community_first_level_50000_18.out", "community_first_level_50000_20.out"]
second_level_file_names = ["community_second_level_50000_5.out", "community_second_level_50000_8.out", "community_second_level_50000_10.out", "community_second_level_50000_13.out", "community_second_level_50000_15.out", "community_second_level_50000_18.out", "community_second_level_50000_20.out"]
golden_standard = []
golden_standard.append(first_level_file_names)
golden_standard.append(second_level_file_names)

# read the input files from the 10 folds
f = open("RunNMI", "w+")
f.write("#!/bin/bash\n")

for k in range(2):  # for each level of golden standard
    f.write("printf \"Ground truth level ")
    f.write(str(k) + "\\n\\n\" \n")
    for j in range(len(output_file_names)):  # for each graph
        f.write("printf \"" + output_file_names[j] + "\\n\" \n")
        for i in range(10):  # for each run
            file1 = str(i) + "/" + output_file_names[j]
            file2 = golden_standard[k][j]
            f.write("../nmi/onmi " + file1 + " " + file2 + "\n")


f.close()

