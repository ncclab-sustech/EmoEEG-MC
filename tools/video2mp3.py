from __future__ import print_function, division
import os
import sys
import subprocess


def class_process(dir_path, dst_dir_path, class_name):
    src_class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(src_class_path):
        print(src_class_path)
        return
    dst_class_path = os.path.join(dst_dir_path, class_name)
    if not os.path.exists(dst_class_path):
        os.makedirs(dst_class_path)
    for file_name in os.listdir(src_class_path):
        if '.mp4' not in file_name:
            continue
        name, ext = os.path.splitext(file_name)
        music_file_name = name + '.mp3'
        video_file_path = os.path.join(src_class_path, file_name)
        music_file_path = os.path.join(dst_class_path, music_file_name)
        cmd = 'ffmpeg -i \"{}\" \"{}\"'.format(video_file_path, music_file_path)
        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')


if __name__ == "__main__":
    # dir_path = sys.argv[1]  # avi directory
    # dst_dir_path = sys.argv[2]  # jpg directory
    dir_path = "seg_dataset/mp4"
    dst_dir_path = "seg_dataset/mp3"
    # class_process(dir_path, dst_dir_path, class_name)
    #print(sys.argv)

    #class_name = sys.argv[1]
    # print(os.listdir(dir_path))
    # for class_name in os.listdir(dir_path):
    #     class_process(dir_path, dst_dir_path, class_name)

    class_process(dir_path, dst_dir_path, 'Joy')
