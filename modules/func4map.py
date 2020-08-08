from PIL import Image,ImageDraw,ImageFont
import math
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
        x=int(landing_point[0]*0.01)
        y=int(landing_point[1]*0.01)
        draw.ellipse((x-30,y-30,x+30,y+30), outline=(0, 0, 0), fill=color_map[str(landing_point[4])])
        # draw.text(xy, text, fill=None, font=None)
        font = ImageFont.truetype("./font/Myriad Pro Bold SemiExtended.ttf", 40)
        draw.text((x+40,y-40), landing_point[3], fill="black",font=font)
    return map_img

def draw_aircraft_path(map_img, aircraft_path_list):
    draw = ImageDraw.Draw(map_img)
    first_point=aircraft_path_list[0]
    last_point=aircraft_path_list[len(aircraft_path_list)-1]

    # air craft path
    Vx=last_point[0]-first_point[0]
    Vy=last_point[1]-first_point[1]
    a=Vy/Vx
    b=first_point[1]-a*first_point[0]
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
            last_point[0]*0.01,
            last_point[1]*0.01,
            last_point[0]*0.01-Uy*200-Ux*500,
            last_point[1]*0.01+Ux*200-Uy*500
        ), fill="white", width=20)
    draw.line(
        (
            last_point[0]*0.01,
            last_point[1]*0.01,
            last_point[0]*0.01+Uy*200-Ux*500,
            last_point[1]*0.01-Ux*200-Uy*500
        ), fill="white", width=20)
    return map_img


def draw_routing_path(map_img, routing_path_list, roster_list, team_id):
    draw = ImageDraw.Draw(map_img)
    # Filter for one team(player name)
    team_roster_list=list(filter(lambda x: x[0]==team_id, roster_list))

    # Filter for one team(routing path)
    team_routing_path_list=list(filter(lambda x: x[4]==team_id, routing_path_list))

    for i in team_roster_list:
        player_routing_path_list=list(filter(lambda x: x[4]==i[1], team_routing_path_list))
        for j in player_routing_path_list:
            
