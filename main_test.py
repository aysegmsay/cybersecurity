import file_object
signature_list="Signature_list.csv"
F1 = file_object.FileClass("Files/test.pdf")  # test
F1.print_file_name()
F1.print_entropy()
F1.print_signature()
F1.print_file_size()
F1.print_file_md5()
F1.print_file_sha1()
F1.print_file_sha256()
F1.print_file_name()
F1.print_file_strings()
