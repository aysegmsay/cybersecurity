import file_object
signature_list="Signature_list.csv"
F1 = file_object.FileClass("Files/test.pdf")  # test
F1.print_entropy()
F1.print_signature()
F1.print_file_size()



