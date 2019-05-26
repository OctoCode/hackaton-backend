from flask import jsonify
import stats


def poisson_binomial_distribution(request):
    request_json = request.get_json()
    res = compute_poisson_binomial(request_json)
    return jsonify(res)


def compute_poisson_binomial(probabilities):
    dist = stats.pbinom(probabilities)
    x = range(len(probabilities))
    return dist.pmf(x).tolist()
