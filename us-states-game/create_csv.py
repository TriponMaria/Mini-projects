import pandas
import turtle

# data_dict = {
#     "state":['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
#              'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
#              'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
#              'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
#              'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
#              'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],
#     "x": [],
#     "y": []
# }
#
#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#     data_dict["x"].append(x)
#     data_dict["y"].append(y)
#
#
# screen = turtle.Screen()
# screen.setup(width=725, height=491)
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data_dict = {'state': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'], 'x': [148.0, -225.0, -204.0, 53.0, -304.0, -111.0, 296.0, 277.0, 229.0, 195.0, -313.0, -222.0, 92.0, 136.0, 31.0, -33.0, 152.0, 60.0, 319.0, 273.0, 311.0, 149.0, 27.0, 96.0, 62.0, -162.0, -44.0, -266.0, 302.0, 282.0, -122.0, 238.0, 241.0, -59.0, 175.0, -12.0, -301.0, 220.0, 313.0, 223.0, -54.0, 112.0, -37.0, -192.0, 287.0, 242.0, -272.0, 199.0, 73.0, -147.0], 'y': [-81.0, -179.0, -34.0, -40.0, 22.0, 24.0, 96.0, 43.0, -142.0, -79.0, -142.0, 128.0, 43.0, 38.0, 81.0, 17.0, -0.0, -117.0, 174.0, 28.0, 112.0, 112.0, 154.0, -83.0, 10.0, 166.0, 60.0, 73.0, 127.0, 63.0, -43.0, 112.0, -17.0, 166.0, 55.0, -33.0, 146.0, 70.0, 97.0, -56.0, 115.0, -33.0, -99.0, 39.0, 142.0, 16.0, 198.0, 29.0, 118.0, 92.0]}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("US_states.csv")