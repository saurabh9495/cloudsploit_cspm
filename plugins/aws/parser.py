import os
import time
import re
import csv

header = ['title', 'category', 'domain', 'description',
          'more_info', 'recommended_action', 'link', 'apis']

with open('parsed_data.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    counter = 0

    for root, dirs, files in os.walk('/Users/saurabhkumar/Downloads/started_wifi/cloudsploit_cspm/plugins/aws'):

        # print("----------------------------------------------------")
        # print(root, dirs, files)

        for file in files:

            if file.endswith('.js') and not file.endswith('.spec.js'):
                data = []
                data_dict = {}
                # print(os.path.join(root, file))
                # os.system('python3 ' + os.path.join(root, file))
                filename = os.path.join(root, file)
                file_ = open(filename, 'r')
                # content = file_.read()
                # print(content)
                line = file_.readline()

                while True:
                    line = file_.readline()

                    if line == '':
                        break
                    # print(line)
                    match_title = re.search(
                        r"title", line, re.MULTILINE | re.DOTALL)

                    if match_title:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"title"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                        except Exception as e:
                            print(e)
                            data_dict[str(counter)+"title"] = "NA"
                    match_category = re.search(
                        r"category", line, re.MULTILINE | re.DOTALL)

                    if match_category:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"category"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                        except Exception as e:
                            print(e)
                            data_dict[str(counter)+"category"] = "NA"
                    match_domain = re.search(
                        r"domain", line, re.MULTILINE | re.DOTALL)

                    if match_domain:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"domain"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                        except Exception as e:
                            print(e)
                            data_dict[str(counter)+"domain"] = "NA"
                    match_description = re.search(
                        r"description", line, re.MULTILINE | re.DOTALL)

                    if counter == 252:
                        data_dict[str(counter)+"domain"] = "NA"

                    if counter == 340:
                        data_dict[str(counter)+"domain"] = "NA"

                    if match_description:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"description"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                        except Exception as e:
                            print(e)
                            data_dict[str(counter)+"description"] = "NA"
                    match_more_info = re.search(
                        r"more_info", line, re.MULTILINE | re.DOTALL)

                    if match_more_info:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"more_info"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                        except Exception as e:
                            print(e)
                            data_dict[str(counter)+"more_info"] = "NA"
                    match_recommended_action = re.search(
                        r"recommended_action", line, re.MULTILINE | re.DOTALL)

                    if match_recommended_action:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"recommended_action"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                        except Exception as e:
                            print(e)
                            data_dict[str(counter) +
                                      "recommended_action"] = "NA"
                    match_link = re.search(
                        r"link", line, re.MULTILINE | re.DOTALL)

                    if match_link:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"link"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                        except Exception as e:
                            print(e)
                            data_dict[str(counter)+"link"] = "NA"

                    if counter == 20:
                        data_dict[str(
                            counter)+"link"] = 'https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html'

                    if counter == 21:
                        data_dict[str(
                            counter)+"link"] = 'https://docs.aws.amazon.com/secretsmanager/latest/userguide/asm_access.html'

                    if counter == 22:
                        data_dict[str(
                            counter)+"link"] = 'https://docs.aws.amazon.com/secretsmanager/latest/userguide/data-protection.html'

                    match_apis = re.search(
                        r"apis", line, re.MULTILINE | re.DOTALL)

                    if match_apis:
                        try:
                            # print(((line.split(':', 1)[1]).strip())[1:-2])
                            data_dict[str(counter)+"apis"] = (
                                ((line.split(':', 1)[1]).strip())[1:-2])
                            break
                        except Exception as e:
                            print(e)
                            data_dict[str(counter)+"apis"] = "NA"
                            break
                # write the data
                # print(data_dict)
                try:
                    data.append(data_dict[str(counter)+"title"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                try:
                    data.append(data_dict[str(counter)+"category"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                try:
                    data.append(data_dict[str(counter)+"domain"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                try:
                    data.append(data_dict[str(counter)+"description"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                try:
                    data.append(data_dict[str(counter)+"more_info"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                try:
                    data.append(data_dict[str(counter)+"recommended_action"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                try:
                    data.append(data_dict[str(counter)+"link"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                try:
                    data.append(data_dict[str(counter)+"apis"])
                except Exception as e:
                    print(os.path.join(root, file))
                    print(e)
                writer.writerow(data)
                counter += 1
                file_.close()
                # time.sleep(1)
