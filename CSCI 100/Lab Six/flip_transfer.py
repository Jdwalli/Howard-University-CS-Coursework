def flip_transfer_list(original, copy):

  original.reverse()
  for i in original:
    copy.append(i)
  
     
  original.clear()