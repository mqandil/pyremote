import requests
from bs4 import BeautifulSoup

def get_html(mlb_url):
    #Stores HTML from Link
    mlb_data = requests.get(mlb_url)
    mlb_html = mlb_data.text

    #Finds HTML for Games
    mlb_bs4 = BeautifulSoup(mlb_html, features="lxml")
    return mlb_bs4

class ParseHtml():
    def __init__(self):
        #Url for Data
        mlb_url = 'https://www.mlb.com'
        self.mlb_bs4 = get_html(mlb_url)

    def get_mlb_live_links(self):
        #Creates Link of Live Links for MLB Games
        mlb_live_links_soup = self.mlb_bs4.find_all(class_=['linkstyle__AnchorElement-sc-1rt6me7-0 lcFuuA getProductButtons__ButtonLink-sc-bgnczd-1 elIcfn trk-button_mlbtv'])
        mlb_live_links_list = []
        for soup in mlb_live_links_soup:
            mlb_live_links_list.append(soup['href'])
        return mlb_live_links_list

    def get_team_matchups(self):
        #Get Teams
        mlb_team_matchups_list = []
        for mlb_team_matchups in self.mlb_bs4.find_all(class_=['TeamWrappersstyle__DesktopTeamWrapper-sc-uqs6qh-0 iNsMPL']):
            mlb_team_matchups_list.append(mlb_team_matchups.text)
        return mlb_team_matchups_list

    def get_scores(self):
        #Get Scores
        mlb_scores_list = []
        for mlb_scores in self.mlb_bs4.find_all(class_=['TeamMatchupLayerstyle__ScoreWrapper-sc-3lvmzz-3 cLonxp']):
            mlb_scores_list.append(mlb_scores.text)
        return mlb_scores_list

    def get_innings(self):
        #Get Innings / See Final Games Here
        mlb_innings_list = []
        for mlb_innings in self.mlb_bs4.find_all(class_=['GameDataLayerstyle__GameStateBaseLabelWrapper-sc-1vhdg11-5 jxEhSY']):
            mlb_innings_list.append(mlb_innings.text)
        return mlb_innings_list

    def get_runners(self):
        #Who's on Base
        mlb_runners_list = []
        for mlb_runner in self.mlb_bs4.find_all(class_=['basepathsstyle__StyledBaseSVG-sc-9dvd8i-0 cYQmUg']):
            mlb_runners_list.append(mlb_runner['aria-label'])
        return mlb_runners_list

    def get_outs(self):
        #Out Count
        mlb_outs_list = []
        for mlb_outs in self.mlb_bs4.find_all(class_=['outsstyle__StyledBaseSVG-sc-4uh89f-0 clvNyU']):
            mlb_outs_list.append(mlb_outs['aria-label'])
        return mlb_outs_list


if __name__ == '__main__':
    test = ParseHtml()
    test2 = test.get_outs()
    print(test2)