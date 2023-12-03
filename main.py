def count_batteries_by_health(present_capacities):
  #Initialization of rated capacity
  rated_capacity = 120    

  #Initialization of the conditional counts
  healthy_count = 0
  exchange_count = 0
  failed_count = 0

  for present_capacity in present_capacities:
    #Calculation of the SoH percentage 
    soh_percentage = (present_capacity/rated_capacity)*100    

    #Classify the batteries base on the SoH percentage
    if soh_percentage > 80:       
      healthy_count += 1
    elif 62 <= soh_percentage <= 80:
      exchange_count += 1
    else:
      failed_count += 1

  #Return the classified counts
  return {
    "healthy": healthy_count,
    "exchange": exchange_count,
    "failed": failed_count
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
