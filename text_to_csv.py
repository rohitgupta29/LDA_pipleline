


import csv
class Splitter():
    def split(self):
        with open('spark.txt', 'r',encoding='utf-8') as in_file:
            lines = [x for x in in_file.read().strip().split('.') if x]
            with open('spark_check.csv', 'w', encoding='utf-8') as out_file:
                writer = csv.writer(out_file, delimiter=',')
                writer.writerow(('ID', 'text'))
                for idx, line in enumerate(lines, 1):
                    writer.writerow((idx, line.strip('.')))





                #
                # writer = csv.writer(out_file)
                # writer.writerow(('title', 'intro'))
                # writer.writerows(lines)


s = Splitter()
s.split()


#
# def split():
#     #Writing to CSV
#     with open('spark.txt',encoding='utf-8') as file_, open('spark.csv', 'w') as csvfile:
#         lines = [x for x in file_.read().strip().split('.') if x]
#         writer = csv.writer(csvfile, delimiter=',')
#         writer.writerow(('ID', 'text'))
#         for idx, line in enumerate(lines, 1):
#             writer.writerow((idx, line.strip('.')))
#
# sentence_splitter = split
#
# print(sentence_splitter)