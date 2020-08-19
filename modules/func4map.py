from PIL import Image,ImageDraw,ImageFont
import math
from datetime import datetime,timedelta
def load_map(map_name):
    # Baltic_Main, Desert_Main, DihorOtok_Main, Erangel_Main, Range_Main, Savage_Main, Summerland_Main 
    path_map={
        "Desert_Main":"./map/Miramar_Main_High_Res.png",
        "Baltic_Main":"./map/Erangel_Remastered_Main_High_Res.png"
    }
    img = Image.open(path_map[map_name])
    img = img.convert("RGB")
    return img

def resize_map(img):
    # img = img.resize((5000, 5000))
    img = img.resize((2000, 2000))
    return img

def draw_landing_point(map_img, landing_point_list):
    color_map={
        "1":"fuchsia",
        "2":"Lime",
        "3":"Blue",
        "4":"maroon",
        "5":"olive",
        "6":"red",
        "7":"green",
        "8":"navy",
        "9":"yellow",
        "10":"aqua",
        "11":"blueviolet",
        "12":"purple",
        "13":"teal",
        "14":"silver",
        "15":"black",
        "16":"orangered"
    }
    draw = ImageDraw.Draw(map_img)
    for landing_point in landing_point_list:
        x=int(landing_point['x']*0.01)
        y=int(landing_point['y']*0.01)
        draw.ellipse((x-30,y-30,x+30,y+30), outline=(0, 0, 0), fill=color_map[str(landing_point['team_id'])])
        font = ImageFont.truetype("./font/Myriad Pro Bold SemiExtended.ttf", 40)
        draw.text((x+40,y-40), landing_point['name'], fill="black",font=font)
    return map_img

def draw_aircraft_path(map_img, aircraft_path_list):
    draw = ImageDraw.Draw(map_img)
    first_point=aircraft_path_list[0]
    last_point=aircraft_path_list[len(aircraft_path_list)-1]

    # air craft path
    Vx=last_point['x']-first_point['x']
    Vy=last_point['y']-first_point['y']
    a=Vy/Vx
    b=first_point['y']-a*first_point['x']
    start_point_x=0
    start_point_y=b
    end_point_x=816000
    end_point_y=816000*a+b
    draw.line(
        (
            start_point_x*0.01,
            start_point_y*0.01,
            end_point_x*0.01,
            end_point_y*0.01
        ), fill="white", width=20)

    # arrow
    V=math.sqrt(Vx*Vx+Vy*Vy)
    Ux=Vx/V
    Uy=Vy/V
    draw.line(
        (
            last_point['x']*0.01,
            last_point['y']*0.01,
            last_point['x']*0.01-Uy*200-Ux*500,
            last_point['y']*0.01+Ux*200-Uy*500
        ), fill="white", width=20)
    draw.line(
        (
            last_point['x']*0.01,
            last_point['y']*0.01,
            last_point['x']*0.01+Uy*200-Ux*500,
            last_point['y']*0.01-Ux*200-Uy*500
        ), fill="white", width=20)
    return map_img


def draw_routing_path(map_img, routing_path_list, landing_point_list, team_roster_list, game_state_list):
    color_map={
        "0":"maroon",
        "1":"fuchsia",
        "2":"Lime",
        "3":"Blue"
    }
    # loading map
    draw=ImageDraw.Draw(map_img)

    # Filter for one team(routing path)
    team_routing_path_list=list(filter(lambda x: x['team_id']==team_roster_list[0]['team_id'], routing_path_list))

    for num,i in enumerate(team_roster_list):
        player_landing_point=list(filter(lambda x: x['name']==i['name'], landing_point_list))
        player_landig_timestamp=datetime.strptime(player_landing_point[0]['timestamp'],'%Y-%m-%dT%H:%M:%S.%fZ')
        player_routing_path_list=list(filter(lambda x: x['name']==i['name'], team_routing_path_list))
        path_list=[]
        path_bool=False
        circle_phase1_end=list(filter(lambda x: x['isGame']==1.5, game_state_list))
        circle_phase1_bool=True
        circle_phase2_end=list(filter(lambda x: x['isGame']==2.5, game_state_list))
        # Landing Point to Phase2
        path_list.append(player_landing_point[0]['x']*0.01)
        path_list.append(player_landing_point[0]['y']*0.01)
        for j in player_routing_path_list:
            if player_landig_timestamp<=datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ'):
                path_bool=True
            if path_bool:
                path_list.append(j['x']*0.01)
                path_list.append(j['y']*0.01)
            if circle_phase1_bool and datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')>=datetime.strptime(circle_phase1_end[len(circle_phase1_end)-1]['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ'):
                phase1_end_position=j
                circle_phase1_bool=False
            if datetime.strptime(j['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ')>=datetime.strptime(circle_phase2_end[len(circle_phase2_end)-1]['timestamp'], '%Y-%m-%dT%H:%M:%S.%fZ'):
                phase2_end_position=j
                break
        draw.line(path_list,fill=color_map[str(num)],width=10)

        # Draw phase1 end position
        try:
            x=phase1_end_position['x']*0.01
            y=phase1_end_position['y']*0.01
            draw.ellipse((x-20,y-20,x+20,y+20), outline=(0, 0, 0), fill="whitesmoke")
        except UnboundLocalError:
            pass

        # Draw phase2 end position
        try:
            x=phase2_end_position['x']*0.01
            y=phase2_end_position['y']*0.01
            draw.ellipse((x-20,y-20,x+20,y+20), outline=(0, 0, 0), fill="lightgray")
        except UnboundLocalError:
            pass

        # Draw landing point and player name
        try:
            x=player_landing_point[0]['x']*0.01
            y=player_landing_point[0]['y']*0.01
            draw.ellipse((x-20,y-20,x+20,y+20), outline=(0, 0, 0), fill="Black")
            font = ImageFont.truetype("./font/Myriad Pro Bold SemiExtended.ttf", 40)
            draw.text((x+40,y-40), i['name'], fill="black",font=font)
        except UnboundLocalError:
            pass
    return map_img

def draw_circle_position(map_img, game_state_list):
    circle_phase1=list(filter(lambda x: x['isGame']==1, game_state_list))
    circle_phase2=list(filter(lambda x: x['isGame']==2, game_state_list))
    draw = ImageDraw.Draw(map_img)
    draw.arc((
        circle_phase1[0]['poisonGasWarningPosition_x']*0.01-circle_phase1[0]['poisonGasWarningPosition_radius']*0.01,
        circle_phase1[0]['poisonGasWarningPosition_y']*0.01-circle_phase1[0]['poisonGasWarningPosition_radius']*0.01,
        circle_phase1[0]['poisonGasWarningPosition_x']*0.01+circle_phase1[0]['poisonGasWarningPosition_radius']*0.01,
        circle_phase1[0]['poisonGasWarningPosition_y']*0.01+circle_phase1[0]['poisonGasWarningPosition_radius']*0.01
        ), start=0, end=360, fill="whitesmoke",width=10)
    draw.arc((
        circle_phase2[0]['poisonGasWarningPosition_x']*0.01-circle_phase2[0]['poisonGasWarningPosition_radius']*0.01,
        circle_phase2[0]['poisonGasWarningPosition_y']*0.01-circle_phase2[0]['poisonGasWarningPosition_radius']*0.01,
        circle_phase2[0]['poisonGasWarningPosition_x']*0.01+circle_phase2[0]['poisonGasWarningPosition_radius']*0.01,
        circle_phase2[0]['poisonGasWarningPosition_y']*0.01+circle_phase2[0]['poisonGasWarningPosition_radius']*0.01
        ), start=0, end=360, fill="lightgray",width=10)
    return map_img
