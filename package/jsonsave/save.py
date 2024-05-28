import json
class JsonSave():
  def __init__(self):

        self.opponent_1_name=""
        self.opponent_2_name= ""
        self.canvas_pic_path=""
        self.from_path_opp1_pic=""
        self.from_path_opp2_pic=""
        self.pict_opp_1=""
        self.pict_opp_2=""
        self.gameblock1=[]
        self.gameblock2=[]
        self.gameblock3=[]
        self.gameblock4=[]
        self.gameblock5=[]
        self.gameblock6=[]
        self.gameblock7=[]
        self.gameblock8=[]
        self.gameblock9=[]
        self.FieldsWin=[]
        self.buttonIndex=0
#collecting data -> parse on json-> send to json file. done.
#json file -> json class -> init of other blocks

  def save_data(self, opponent_1_name, opponent_2_name,path1,path2,pict_opp_1,pict_opp_2,canvas,blocks,FieldsWin,last_index):
      data = {
          "opponent_1_name": opponent_1_name,
          "opponent_2_name": opponent_2_name,
          "from_path_opp1_pic": path1,
          "from_path_opp2_pic": path2,
          "pict_opp_1": pict_opp_1,
          "pict_opp_2": pict_opp_2,
          "canvas_pic": canvas,
          "gameblock1": [button.text() for button in blocks[0][0].buttons],
          "gameblock2": [button.text() for button in blocks[0][1].buttons],
          "gameblock3": [button.text() for button in blocks[0][2].buttons],
          "gameblock4": [button.text() for button in blocks[1][0].buttons],
          "gameblock5": [button.text() for button in blocks[1][1].buttons],
          "gameblock6": [button.text() for button in blocks[1][2].buttons],
          "gameblock7": [button.text() for button in blocks[2][0].buttons],
          "gameblock8": [button.text() for button in blocks[2][1].buttons],
          "gameblock9": [button.text() for button in blocks[2][2].buttons],
          "FieldsWin": FieldsWin,
          "last_index": last_index,
      }
      with open("C:/Users/egori/source/repos/labs_qt/package/jsonsave/out.json", "w") as f:
          json.dump(data, f,indent=2)
  def load_data(self):
    try:
        with open("C:/Users/egori/source/repos/labs_qt/package/jsonsave/out.json", "r") as f:
            data = json.load(f)
            self.opponent_1_name = data["opponent_1_name"]
            self.opponent_2_name = data["opponent_2_name"]
            self.canvas_pic_path = data["canvas_pic"]
            self.from_path_opp1_pic=data["from_path_opp1_pic"]
            self.from_path_opp2_pic=data["from_path_opp2_pic"]
            self.pict_opp_1 = data["pict_opp_1"]
            self.pict_opp_2 = data["pict_opp_2"]
            self.gameblock1=data["gameblock1"]
            self.gameblock2=data["gameblock2"]
            self.gameblock3=data["gameblock3"]
            self.gameblock4=data["gameblock4"]
            self.gameblock5=data["gameblock5"]
            self.gameblock6=data["gameblock6"]
            self.gameblock7=data["gameblock7"]
            self.gameblock8=data["gameblock8"]
            self.gameblock9=data["gameblock9"]
            self.FieldsWin=data["FieldsWin"]
            self.buttonIndex=data["last_index"]
    except FileNotFoundError:
        pass