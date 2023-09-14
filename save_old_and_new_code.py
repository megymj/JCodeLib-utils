import os
import subprocess
import shutil
import csv


def read_csv(file_name):
    data_list = []
    with open(file_name, mode='r', encoding='utf-8-sig') as file:
        # Create a CSV DictReader object
        csvreader = csv.DictReader(file)

        # Fetching each row one by one
        for row in csvreader:
            data_dict = {
                'project_name': row['project_name'],
                'file_id': row['file_id'],
                'file_path': row['file_path'],
                'old_commit': row['old_commit'],
                'new_commit': row['new_commit'],
            }
            data_list.append(data_dict)
    return data_list


if __name__ == "__main__":
    csv_read = read_csv('data/old_new_commits.csv')

    for i in csv_read:

        # Create dir
        # file id에 대해 동일한 *.java 파일이 존재하므로, 구분하기 위해 각 file id마다 저장
        destination_path_old = 'project/' + i['project_name'] + '/old/' + i['file_id']
        destination_path_new = 'project/' + i['project_name'] + '/new/' + i['file_id']
        if not os.path.exists(destination_path_old):
            os.mkdir(destination_path_old)
        if not os.path.exists(destination_path_new):
            os.mkdir(destination_path_new)

        # Move to target folder
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        os.chdir(desktop + '/' + i['project_name'])

        '''checkout to old commit'''
        subprocess.run(['git', 'checkout', i['old_commit']])

        # Define the source file and destination directory
        source_file_old = os.path.join(desktop, i['project_name'], i['file_path'])
        destination_dir_old = os.path.join(desktop, 'SELAB/JCodeLib-utils/project/', i['project_name'],
                                           'old', i['file_id'])

        # Use shutil's copy2 function to copy the file
        shutil.copy2(source_file_old, destination_dir_old)

        '''checkout to new commit'''
        subprocess.run(['git', 'checkout', i['new_commit']])

        source_file_new = os.path.join(desktop, i['project_name'], i['file_path'])
        destination_dir_new = os.path.join(desktop, 'SELAB/JCodeLib-utils/project/', i['project_name'],
                                           'new', i['file_id'])
        shutil.copy2(source_file_new, destination_dir_new)

        # checkout to master branch
        subprocess.run(['git', 'checkout', 'master'])

        # move on to origin path
        os.chdir(desktop + '/SELAB/JCodeLib-utils/')
