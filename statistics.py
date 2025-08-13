import statistics

def calculate_statistics(data):
  """
  Calculates the mean and median of a list of numbers.

  Args:
    data: A list of numbers.

  Returns:
    A dictionary with the mean and median.
  """
  mean = statistics.mean(data)
  median = statistics.median(data)
  return {"mean": mean, "median": median}