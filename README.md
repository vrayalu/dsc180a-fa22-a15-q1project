# DSC180A FA22 A15 Project

About Project:
Recent work introduced the vast unfolding of communities in large networks, in which a heuristic methodology not only identifies communities, but also measures the density between nodes in modules that highlight the strength of a subcommunity. It was shown that such methodology can facilitate community detection, and exceed similar community detection algorithms in time complexity. In this paper, we introduce a more simplistic foundation based algorithm, in which communities are identified through the metric of common neighbors. We show how a collection of nodes with a large number of common neighbors have a higher probability of being deemed a community. Our algorithms are first trained from simple randomly generated graphs with ground truths. In training, we derive a 50% threshold for the proportion of common neighbors within nodes to be identified as a community. We apply these algorithms to real world graphs to visualize and represent our results.


The report can be found in `bin/report.pdf`

To run the code and generate the report, run this command:

`python run.py report`


