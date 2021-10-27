
from graphs import *

if __name__ == "__main__":
    print("Simulation started at {}".format(datetime.now().strftime("%H:%M:%S")))
    start_time = time.perf_counter()

    # These are examples of simulations you could run. The heatmap ones take a while to calculate
    # for i in range(10):
    single_simulation(algorithm="baseline", number_of_people=10, number_of_floors=4,
                  max_elevator_capacity=1, animate=True, animation_speed=0.8)
    # for i in range(10):
    #     single_simulation(algorithm="efficient", number_of_people=5, number_of_floors=10,
    #                       max_elevator_capacity=6, animate=True, animation_speed=0.1)
    # googleData = googleData = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.1478599999999588, 0.3324724999999482, 0.31588499999988784, 0.40488125000015174, 0.4408439999996858, 0.4632375000001048, 0.48321785714274057, 0.5270712499999348, 0.6180966666665242, 0.7189775000000367], [0.0, 0.5114149999999, 0.8952099999997998, 1.0104150000002576, 1.1843924999996318, 1.4532000000001517, 1.723438333333199, 1.9446064285712836, 2.164335624999424, 2.5004394444439555, 2.7795100000000588], [0.0, 0.9950099999999367, 1.5262799999999785, 1.7760283333328957, 2.276964999999791, 2.678139999999246, 3.1386150000003283, 3.5424685714285573, 4.096370625001001, 4.422652222222155, 5.0651325000012974], [0.0, 1.4718850000002064, 2.2467450000000966, 2.5081949999999864, 3.1929675000005915, 3.8847440000003672, 4.692472500000434, 5.3339164285716265, 6.181968750000152, 6.601488888890117, 7.314768000000129], [0.0, 1.9520449999995293, 3.0342474999998785, 3.327548333333283, 4.340904999999523, 5.302939000001231, 6.196244166668237, 6.9354807142865695, 8.130542499998569, 9.11138388889006, 10.065668500000044], [0.0, 2.281740000000255, 3.7517299999998244, 4.338938333333317, 5.549599999999344, 6.508199999998908, 7.4402333333327135, 9.239783571428603, 9.995728749999358, 11.302448333333615, 12.61807000000212], [0.0, 2.7540149999996544, 4.594975000000446, 4.991185000000144, 6.401086250000361, 7.826797999999286, 8.996411666665296, 10.444778571428799, 11.835434374999721, 12.944426111111596, 15.180111500000805], [0.0, 3.5947549999994237, 5.211859999999618, 6.169868333332602, 7.575751250001076, 9.13548500000121, 10.738267500001456, 12.676480714287493, 14.022852499998521, 15.855802222222053, 17.070300499999348], [0.0, 3.912569999999505, 6.1479325000001666, 6.9213433333325725, 8.670201250000105, 10.23498300000199, 12.133558333332019, 14.667809285714839, 15.817481875000624, 18.794696111108635, 19.957344999999123], [0.0, 4.513859999999951, 6.664195000000461, 7.817095000001245, 9.916148749998626, 11.757223000001801, 13.780929166666624, 16.38555214285867, 17.807773124997368, 21.117410555556432, 22.560298999999247]]

    # heatmap("baseline", 5, 5)
    # heatmap("efficient", 50, 50)
    # heatmap("efficient", 100, 100)
    # heatmap("baseline", 100, 100)

    # heatmap_comparison(max_people=47, max_floors=47)
    # interpolate_heatmap(*heatmap_comparison(max_people=100, max_floors=100))
    #
    # graph_single_algorithm_histogram("baseline", people=30, floors=10, iterations=100_000)
    # graph_one_algorithm_frequency_curve("baseline", 30, 10, 10_000)
    # graph_both_algorithms_frequency_curve(30, 10, 100_000)
    # boxplot_comparison(30, 10, 1_000)

    finish_time = time.perf_counter()
    print('Total time taken: {}s'.format(finish_time - start_time))
