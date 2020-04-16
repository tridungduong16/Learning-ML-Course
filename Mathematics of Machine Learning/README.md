
# Mathematics of Machine Learning:
# Table of Contents
1. [The Statistical Theory of Machine Learning. ](#intrinsic)
2. [Classification, Regression, Aggregation](#intrinsic)
3. [Empirical Risk Minimization, Regularization](#empirical)
4. [Suprema of Empirical Processes](#intrinsic)
5. [Algorithms and Convexity. ](#intrinsic)
6. [Boosting](#intrinsic)
7. [Kernel Methods](#intrinsic)
8. [Convex Optimization](#intrinsic)
9. [Online Learning. ](#intrinsic)
10. [Online Convex Optimization](#intrinsic)
11. [Partial Information: Bandit Problems](#intrinsic)
12. [Blackwell's Approachability](#intrinsic)


## Formulations <a name="Formulations"></a>

## Empirical Risk Minimization, Regularization <a name="empirical"></a>

Empirical risk minimization (ERM) is a principle in statistical learning theory which defines a family of learning algorithms and is used to give theoretical bounds on their performance. The core idea is that we cannot know exactly how well an algorithm will work in practice (the true "risk") because we don't know the true distribution of data that the algorithm will work on, but we can instead measure its performance on a known set of training data (the "empirical" risk).

We assume that our samples come from this distribution and use our dataset as an approximation. If you compute the loss using the data points in our dataset, it’s called empirical risk. It’s “empirical” and not “true” because we are using a dataset that’s a subset of the whole population.

When we build our learning model, we need to pick the function that minimizes the empirical risk i.e. the delta between the predicted output and the actual output for the data points in our dataset. This process of finding this function is called empirical risk minimization. Ideally, we would like to minimize the true risk. But we don’t have the information that allows us to achieve that, so our hope is that this empiricial risk will almost be the same as the true empirical risk. Hence by minimizing it, we aim to minimize the true risk

Link:
  * https://www.mit.edu/~9.520/spring11/slides/class02.pdf
  * https://people.cs.umass.edu/~domke/courses/sml2011/03optimization.pdf
  * http://www.cs.cornell.edu/courses/cs4780/2015fa/web/lecturenotes/lecturenote10.html
