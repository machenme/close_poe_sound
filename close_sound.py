import os

user_home = os.environ["USERPROFILE"]
filepath = os.path.join(
    user_home, r"Documents\My Games\Path of Exile\production_Config.ini"
)
if not os.path.exists(filepath):
    print("file not exist, process end")
    exit(1)
else:
    with open(filepath, "r") as f:
        data = f.readlines()

    change_list = ["music_volume2=", "ambient_sound_volume2=", "sound_effects_volume2="]
    new_data = []
    for line in data:
        for parser in change_list:
            if line.startswith(parser):
                line = parser + "false\n"
                print(line)
        new_data.append(line)
    try:
        os.rename(filepath, filepath + ".bac")
        with open(filepath, "w") as f:
            f.writelines(new_data)
    except FileExistsError:
        os.remove(filepath + ".bac")
        os.rename(filepath, filepath + ".bac")
        with open(filepath, "w") as f:
            f.writelines(new_data)
    print("done")
