def log_reader(log_name):
    result = []

    with open(log_name, 'r', encoding='utf-8') as logs:
        for line in logs:
            search_ip = line.find('-')
            data_ip = line[:searc_ip]

            search_get = line.find('"')
            data_get = line[searc_ip + 1:searc_ip + 4]

            log_line_get = line.find('GET')
            log_line_http = line.find('HTTP')

            data_patch = line[log_line_get:log_line_http]

            result.append(f'{data_ip} {data_get} {data_patch}')
    
    print(result)

    return


log_reader('ngin+x_logs.txt')
