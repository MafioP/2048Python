#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.5 on Sun May 10 13:36:18 2020
#
import windowController
import wx
import os

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade



# end of class newGameFrame
class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        self.tiles = ""
        self.score = 0
        self.moves = 0
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((900, 600))
        self.options_Panel = wx.Panel(self, wx.ID_ANY)
        self.mode_Button = wx.Button(self.options_Panel, wx.ID_ANY, "Change Mode")
        self.save_Button = wx.Button(self.options_Panel, wx.ID_ANY, "Save Game")
        self.menu_Button = wx.Button(self.options_Panel, wx.ID_ANY, "Main Menu")
        self.data_Panel = wx.Panel(self, wx.ID_ANY)
        self.grid_Panel = wx.Panel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_change_mode, self.mode_Button)
        self.Bind(wx.EVT_BUTTON, self.on_save_game, self.save_Button)
        self.Bind(wx.EVT_BUTTON, self.on_main_menu, self.menu_Button)
        # end wxGlade

        self.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)

        self.addData(self.score, self.moves)
        self.SetFocus()

    def addGrid(self):
        grid = wx.GridSizer(len(self.tiles), len(self.tiles), 5, 5)
        print("Cols " + str(grid.GetCols()))
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles)):
                label = wx.StaticText(self.grid_Panel)
                label.SetLabel(self.tiles[j][i].getDisplayValue())
                grid.Add(label, 1, wx.EXPAND, 5)
        self.grid_Panel.SetSizer(grid)
        self.Layout()

    def addData(self, score, moves):
        print("Score:", score)
        print("Moves:", moves)
        dataSizer = wx.BoxSizer(wx.VERTICAL)
        scoreLbl = wx.StaticText(self.data_Panel)
        scoreLbl.SetLabel("Score: " + str(score))
        dataSizer.Add(scoreLbl)
        movesLbl = wx.StaticText(self.data_Panel)
        movesLbl.SetLabel("Moves: " + str(moves))
        dataSizer.Add(movesLbl)
        self.data_Panel.SetSizer(dataSizer)
        self.Layout()

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("2048py Game")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        options_Sizer = wx.BoxSizer(wx.VERTICAL)
        options_Sizer.Add(self.mode_Button, 1, wx.ALL | wx.EXPAND, 4)
        options_Sizer.Add(self.save_Button, 1, wx.ALL | wx.EXPAND, 4)
        options_Sizer.Add(self.menu_Button, 1, wx.ALL | wx.EXPAND, 4)
        self.options_Panel.SetSizer(options_Sizer)
        sizer_3.Add(self.options_Panel, 1, wx.EXPAND, 0)
        sizer_3.Add(self.data_Panel, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(self.grid_Panel, 4, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def on_change_mode(self, event):  # wxGlade: MainFrame.<event_handler>
        print("Event handler 'on_change_mode' not implemented!")
        event.Skip()

    def on_save_game(self, event):  # wxGlade: MainFrame.<event_handler>
        print("Event handler 'on_save_game' not implemented!")
        event.Skip()

    def on_main_menu(self, event):  # wxGlade: MainFrame.<event_handler>
        menu = MenuFrame(None, wx.ID_ANY, "")
        menu.ShowModal()

    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        print("KeyPressed: " + str(keycode))
        if keycode == 87:
            windowController.movement("W", self.score, self.tiles)
            windowController.addValue(self.tiles)
            self.grid_Panel.SetSizer(None, True)
        elif keycode == 65:
            windowController.movement("A", self.score, self.tiles)
            windowController.addValue(self.tiles)
            self.grid_Panel.SetSizer(None, True)
        elif keycode == 83:
            windowController.movement("S", self.score, self.tiles)
            windowController.addValue(self.tiles)
            self.grid_Panel.SetSizer(None, True)
        elif keycode == 68:
            windowController.movement("D", self.score, self.tiles)
            windowController.addValue(self.tiles)
            self.grid_Panel.SetSizer(None, True)
        windowController.board(len(self.tiles), 4, self.tiles)
        windowController.unlockAll(self.tiles)
        self.addData(self.score, self.moves)
        self.addGrid()
        self.Layout()


# end of class MainFrame

class MenuFrame(wx.Dialog):
    def __init__(self, *args, **kwds):
        self.openPath = ""
        self.savePath = ""
        # begin wxGlade: MenuFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((500, 400))
        self.newGameButton = wx.Button(self, wx.ID_ANY, "Start new game")
        self.loadGameButton = wx.Button(self, wx.ID_ANY, "Load game")
        self.exitGameButton = wx.Button(self, wx.ID_ANY, "Exit game")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_start_game, self.newGameButton)
        self.Bind(wx.EVT_BUTTON, self.on_load_game, self.loadGameButton)
        self.Bind(wx.EVT_BUTTON, self.on_exit_game, self.exitGameButton)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MenuFrame.__set_properties
        self.SetTitle("Main Menu")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MenuFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.newGameButton, 1, wx.ALL | wx.EXPAND, 15)
        sizer_2.Add(self.loadGameButton, 1, wx.ALL | wx.EXPAND, 15)
        sizer_2.Add(self.exitGameButton, 1, wx.ALL | wx.EXPAND, 15)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def on_start_game(self, event):  # wxGlade: MenuFrame.<event_handler>
        self.Hide()
        newGame_Frame = newGameFrame(None, wx.ID_ANY, "")
        newGame_Frame.Show()

    def on_load_game(self, event):  # wxGlade: MenuFrame.<event_handler>
        fileDialog = wx.FileDialog(self, message="Choose a file",  defaultDir=os.getcwd(), defaultFile="",
                                   style=wx.FD_OPEN | wx.FD_CHANGE_DIR)
        if fileDialog.ShowModal() == wx.ID_OK:
            self.openPath = fileDialog.GetPath()
            print("You have chosen this file: ", self.openPath)
            fileDialog.Destroy()
        self.Hide()

        self.main_Frame = MainFrame(None, wx.ID_ANY, "")
        self.main_Frame.score, self.main_Frame.moves, self.main_Frame.tiles = windowController.readFile(self.openPath)
        self.main_Frame.addGrid()
        self.main_Frame.Show()


    def on_exit_game(self, event):  # wxGlade: MenuFrame.<event_handler>
        event.Skip()

# end of class MenuFrame


class newGameFrame(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: newGameFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.size_SpinCtrl = wx.SpinCtrl(self, wx.ID_ANY, "4", min=0, max=10)
        self.block_SpinCtrl = wx.SpinCtrl(self, wx.ID_ANY, "2", min=0, max=100)
        self.start_Button = wx.Button(self, wx.ID_ANY, "Start Game")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_start_game, self.start_Button)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: newGameFrame.__set_properties
        self.SetTitle("New Game")
        self.SetSize((400, 300))
        self.size_SpinCtrl.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        self.block_SpinCtrl.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: newGameFrame.__do_layout
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        size_Label = wx.StaticText(self, wx.ID_ANY, "Select Size")
        size_Label.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_6.Add(size_Label, 1, wx.ALL, 15)
        sizer_6.Add(self.size_SpinCtrl, 1, wx.ALL, 15)
        sizer_5.Add(sizer_6, 1, wx.ALL | wx.EXPAND, 5)
        blocks_Label = wx.StaticText(self, wx.ID_ANY, "Select number of \n obstacles")
        blocks_Label.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_7.Add(blocks_Label, 1, wx.ALL, 15)
        sizer_7.Add(self.block_SpinCtrl, 1, wx.ALL, 15)
        sizer_5.Add(sizer_7, 1, wx.ALL | wx.EXPAND, 5)
        sizer_5.Add(self.start_Button, 1, wx.ALIGN_CENTER | wx.ALL, 15)
        self.SetSizer(sizer_5)
        self.Layout()
        # end wxGlade

    def on_start_game(self, event):
        size = self.size_SpinCtrl.GetValue()
        blocks = self.block_SpinCtrl.GetValue()
        self.Hide()
        self.main_Frame = MainFrame(None, wx.ID_ANY, "")
        self.main_Frame.tiles = windowController.setGrid(size, blocks)
        self.main_Frame.addGrid()
        self.main_Frame.Show()


class Window(wx.App):
    def OnInit(self):
        self.menu_Frame = MenuFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.menu_Frame)
        self.menu_Frame.Show()
        return True


# end of class Window

if __name__ == "__main__":
    app = Window(0)
    app.MainLoop()
