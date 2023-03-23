import json
import csv
import datetime

input_file_name = "expoertedjsonfilename.txt"
output_file_name = "outputfilename.csv"

source_json = json.load(open(input_file_name, 'r'))
fields_order = ["Id", "HostName", "HostIp", "Timestamp", "EventType", "ParentStartupParameters",
                "StartupParameters", 'ParentFileFullName', 'FileFullName',
                "UserName", "LogonType", "LogonSessionId", "SignatureCheckResult", "SignatureSubjectName",
                "LocalIp", "LocalPort", "RemoteIp", "RemotePort", "Direction",
                "UniqueParentPid", "UniquePid", "InterpretedFiles",
                'ParentSystemPid', 'SystemPid', 'IntegrityLevel',
                'FileSize', 'FileCreationTime', 'FileModificationTime', 'Md5', 'Sha256', 'FileAttributes',
                'FileType', 'ZoneIdentifier', 'ParentMd5', 'ParentSha256', 'ProductName',
                'ProductVersion', 'OriginalFileName', 'ProductVendor', 'FileDescription', 'FileVersion',
                'SignatureTimestamp', 'AccountType', 'EndTime', 'ReceivedTimestamp', 'Ioa']

with open(output_file_name, 'w') as output:
    output_csv = csv.writer(output)
    output_csv.writerow(fields_order)
    for res in source_json["results"]:
        csv_parse_result = list()
        for field in fields_order:
            try:
                if field in ["Timestamp", 'FileCreationTime', 'FileModificationTime',
                             'SignatureTimestamp', 'EndTime', 'ReceivedTimestamp']:
                    csv_parse_result.append(
                        datetime.datetime.fromtimestamp(int(res[field]) / 1000000.0).strftime("%Y-%m-%d %H:%M:%S"))
                    continue
                if type(res[field]) == list:
                    csv_parse_result.append(str(res[field]).replace(',', ';'))
                else:
                    csv_parse_result.append(res[field])
            except KeyError:
                csv_parse_result.append('')
                continue
            except OSError:
                csv_parse_result.append('')
                continue
        csv.writer(output)
        output_csv.writerow(csv_parse_result)
