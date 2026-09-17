KB = 1024
MB = 1048576
GB = 1073741824

num_entries = float(input("Please enter the number of entries per second: "))
entry_size = float(input("Please enter the average number of bytes per entry: "))

kb_size = (num_entries * 60 * entry_size) / KB
mb_size = (num_entries * 3600 * entry_size) / MB
gb_size = (num_entries * 86400 * entry_size) / GB


print("Storage Estimates:")
print("Per minute: " + str(kb_size) + " KB")
print("Per hour: " + str(mb_size) + " MB")
print("Per day: " + str(gb_size) + " GB")