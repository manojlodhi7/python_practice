# import csv
# with open("C:\\Users\\mlodhi\\OneDrive - Nice Systems Ltd\\Desktop\\Python Pract\\csv_file_01.csv", 'r') as file:
#     data = [row for row in csv.reader(file.read().splitlines())]
#
# for row in data:
#     for v in row:
#         print(v)

#
# import csv
# # l1 = list()
# def csv_reader():
#     with open("C:\\Users\\mlodhi\\OneDrive - Nice Systems Ltd\\Desktop\\Python Pract\\sample.csv",  encoding='utf-8-sig') as f:
#         data = csv.reader(f, delimiter=',')
#         return [row for row in data]
#
#
# def key_value():
#     all_data = csv_reader()
#     column_list = all_data[0]
#     list_of_unique_column_values = {str(v): set() for v in column_list}
#     # print(list_of_unique_column_values)
#     for i in range(1, len(all_data)):
#         row = all_data[i]
#         for j in range(len(row)):
#             key = column_list[j]
#             value = row[j]
#             if value != '':
#                 s = set()
#                 s.add(value)
#                 list_of_unique_column_values.get(key).update(s)
#     # print(list_of_unique_column_values)
#     return list_of_unique_column_values, column_list
#
#
#
# def csv_writer(d, c):
#     with open("C:\\Users\\mlodhi\\OneDrive - Nice Systems Ltd\\Desktop\\Python Pract\\sample_write.csv", 'w', newline='') as f:
#         wr = csv.writer(f, delimiter=',')
#         print(c)
#         wr.writerow([c for c in c])
#         for p in range(5):
#             for i in range(len(d.get(c[0]))):
#                 s = list(d.get(c[0]))[i]
#                 for j in range(len(d.get(c[1]))):
#                     s1 = list(d.get(c[1]))[j]
#                     for k in range(len(d.get(c[2]))):
#                         s2 = list(d.get(c[2]))[k]
#                         for k1 in range(len(d.get(c[3]))):
#                             s3 = list(d.get(c[3]))[k1]
#                             for k2 in range(len(d.get(c[4]))):
#                                 s4 = list(d.get(c[4]))[k2]
#                                 for k3 in range(len(d.get(c[5]))):
#                                     s5 = list(d.get(c[5]))[k3]
#                                     for k6 in range(len(d.get(c[6]))):
#                                         s6 = list(d.get(c[6]))[k6]
#                                         wr.writerow([s, s1, s2, s4, s5, s6])
#
#
#
#
# print(key_value())
# d, c = key_value()
# csv_writer(d, c)




# ********************************************************************************

import csv
# l1 = list()
def csv_reader():
    with open("C:\\Users\\mlodhi\\OneDrive - Nice Systems Ltd\\Desktop\\Python Pract\\python_practice\\PractPackage\\files\\sample.csv",  encoding='utf-8-sig') as f:
        data = csv.DictReader(f, delimiter=',')
        dt = [dict(d) for d in data]
        columns = tuple(dt[0].keys())
        list_of_unique_column_values = {str(v): set() for v in columns}
        for v in range(len(dt)):
            values = list(dt[v].values())
            for i in range(len(values)):
                key = columns[i]
                if values[i] != '':
                    s = set()
                    s.add(values[i])
                    list_of_unique_column_values.get(key).update(s)
        return columns, list_of_unique_column_values


print(csv_reader())


