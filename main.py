from pypresence import Presence
import time, os
import bg_helper

CLIENT_ID = "847859372692602902"


def get_now_playing_data():
    now_playing = bg_helper.run_output("mocp --info", timeout=2)
    data = dict(
        [
            (k.lower(), v.strip())
            for k, v in [line.split(":", 1) for line in now_playing.split("\n") if line]
        ]
    )
    if "fatal_error" in data:
        return ""
    elif "timeout" in data:
        return ""
    elif data.get("state") == "STOP":
        return ""
    return data


def main(CLIENT_ID):
    RPC = Presence(CLIENT_ID)
    data = get_now_playing_data()
    if data != "":
        global icon
        if data["state"] == "PLAY":
            icon = "play"
        elif data["state"] == "PAUSE":
            icon = "pause"
        else:
            icon = "lxmusic"

        albumstr = f"📀 {data['album']}" if len(data["album"]) != 0 else ""
        title = os.path.splitext(os.path.basename(data['file']))[0] if data['songtitle'] == "" else data['songtitle']

        RPC.connect()
        RPC.update(
            large_image="mocp",
            large_text="Music On Console Player",
            buttons=[{"label": "Now Playing", "url": "http://mdvsh.co/hi"}],
            details=f"🎶 {title}",
            state=f"👥 {data['artist']} {albumstr}",
            small_image=f"{icon}",
            small_text="listening to . . .",
        )
    else:
        pass

while True:
    main(CLIENT_ID)
    # can only update rpc every 15 seconds (renders time elapsed param moot)
    # pypresence lacking oof
    time.sleep(15)  
