from main import *


def test_MED():
  for S, T in test_cases:
    assert fast_MED(S, T) == MED(S, T)

    # could not get pytest to work so made own test to print
    if fast_MED(S, T) == MED(S, T):
      print("true")
    


def test_align():
  for i in range(len(test_cases)):
    S, T = test_cases[i]
    align_S, align_T = fast_align_MED(S, T)
    #assert (align_S == alignments[i][0] and align_T == alignments[i][1])
    if (align_S == alignments[i][0] and align_T == alignments[i][1]):
      print("true")


#test_MED()
test_align()
