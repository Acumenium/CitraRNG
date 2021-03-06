# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PokemonDisplay.ui',
# licensing of 'PokemonDisplay.ui' applies.
#
# Created: Sat Feb 23 00:00:09 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_PokemonDisplay(object):
    def setupUi(self, PokemonDisplay):
        PokemonDisplay.setObjectName("PokemonDisplay")
        PokemonDisplay.resize(195, 434)
        self.gridLayout = QtWidgets.QGridLayout(PokemonDisplay)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBoxPokemon = QtWidgets.QGroupBox(PokemonDisplay)
        self.groupBoxPokemon.setObjectName("groupBoxPokemon")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxPokemon)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutCharacteristics = QtWidgets.QGridLayout()
        self.gridLayoutCharacteristics.setObjectName("gridLayoutCharacteristics")
        self.labelSpecies = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpecies.setObjectName("labelSpecies")
        self.gridLayoutCharacteristics.addWidget(self.labelSpecies, 0, 0, 1, 1)
        self.labelSpeciesValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpeciesValue.setObjectName("labelSpeciesValue")
        self.gridLayoutCharacteristics.addWidget(self.labelSpeciesValue, 0, 1, 1, 1)
        self.labelGender = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelGender.setObjectName("labelGender")
        self.gridLayoutCharacteristics.addWidget(self.labelGender, 1, 0, 1, 1)
        self.labelGenderValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelGenderValue.setObjectName("labelGenderValue")
        self.gridLayoutCharacteristics.addWidget(self.labelGenderValue, 1, 1, 1, 1)
        self.labelNature = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelNature.setObjectName("labelNature")
        self.gridLayoutCharacteristics.addWidget(self.labelNature, 2, 0, 1, 1)
        self.labelNatureValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelNatureValue.setObjectName("labelNatureValue")
        self.gridLayoutCharacteristics.addWidget(self.labelNatureValue, 2, 1, 1, 1)
        self.labelAbility = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAbility.setObjectName("labelAbility")
        self.gridLayoutCharacteristics.addWidget(self.labelAbility, 3, 0, 1, 1)
        self.labelAbilityValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAbilityValue.setObjectName("labelAbilityValue")
        self.gridLayoutCharacteristics.addWidget(self.labelAbilityValue, 3, 1, 1, 1)
        self.labelItem = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelItem.setObjectName("labelItem")
        self.gridLayoutCharacteristics.addWidget(self.labelItem, 4, 0, 1, 1)
        self.labelItemValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelItemValue.setObjectName("labelItemValue")
        self.gridLayoutCharacteristics.addWidget(self.labelItemValue, 4, 1, 1, 1)
        self.labelSV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSV.setObjectName("labelSV")
        self.gridLayoutCharacteristics.addWidget(self.labelSV, 5, 0, 1, 1)
        self.labelSVValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSVValue.setObjectName("labelSVValue")
        self.gridLayoutCharacteristics.addWidget(self.labelSVValue, 5, 1, 1, 1)
        self.labelHiddenPower = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHiddenPower.setObjectName("labelHiddenPower")
        self.gridLayoutCharacteristics.addWidget(self.labelHiddenPower, 6, 0, 1, 1)
        self.labelHiddenPowerValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHiddenPowerValue.setObjectName("labelHiddenPowerValue")
        self.gridLayoutCharacteristics.addWidget(self.labelHiddenPowerValue, 6, 1, 1, 1)
        self.labelFriendship = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelFriendship.setObjectName("labelFriendship")
        self.gridLayoutCharacteristics.addWidget(self.labelFriendship, 7, 0, 1, 1)
        self.labelFriendshipValue = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelFriendshipValue.setObjectName("labelFriendshipValue")
        self.gridLayoutCharacteristics.addWidget(self.labelFriendshipValue, 7, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayoutCharacteristics, 1, 0, 1, 1)
        self.pushButtonUpdate = QtWidgets.QPushButton(self.groupBoxPokemon)
        self.pushButtonUpdate.setEnabled(False)
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.gridLayout_2.addWidget(self.pushButtonUpdate, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.gridLayoutMoves = QtWidgets.QGridLayout()
        self.gridLayoutMoves.setObjectName("gridLayoutMoves")
        self.labelMove1 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove1.setObjectName("labelMove1")
        self.gridLayoutMoves.addWidget(self.labelMove1, 0, 0, 1, 1)
        self.labelMove1Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove1Name.setObjectName("labelMove1Name")
        self.gridLayoutMoves.addWidget(self.labelMove1Name, 0, 1, 1, 1)
        self.labelMove1PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove1PP.setObjectName("labelMove1PP")
        self.gridLayoutMoves.addWidget(self.labelMove1PP, 0, 2, 1, 1)
        self.labelMove2 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove2.setObjectName("labelMove2")
        self.gridLayoutMoves.addWidget(self.labelMove2, 1, 0, 1, 1)
        self.labelMove2Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove2Name.setObjectName("labelMove2Name")
        self.gridLayoutMoves.addWidget(self.labelMove2Name, 1, 1, 1, 1)
        self.labelMove2PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove2PP.setObjectName("labelMove2PP")
        self.gridLayoutMoves.addWidget(self.labelMove2PP, 1, 2, 1, 1)
        self.labelMove3 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove3.setObjectName("labelMove3")
        self.gridLayoutMoves.addWidget(self.labelMove3, 2, 0, 1, 1)
        self.labelMove3Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove3Name.setObjectName("labelMove3Name")
        self.gridLayoutMoves.addWidget(self.labelMove3Name, 2, 1, 1, 1)
        self.labelMove3PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove3PP.setObjectName("labelMove3PP")
        self.gridLayoutMoves.addWidget(self.labelMove3PP, 2, 2, 1, 1)
        self.labelMove4 = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove4.setObjectName("labelMove4")
        self.gridLayoutMoves.addWidget(self.labelMove4, 3, 0, 1, 1)
        self.labelMove4Name = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove4Name.setObjectName("labelMove4Name")
        self.gridLayoutMoves.addWidget(self.labelMove4Name, 3, 1, 1, 1)
        self.labelMove4PP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelMove4PP.setObjectName("labelMove4PP")
        self.gridLayoutMoves.addWidget(self.labelMove4PP, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayoutMoves, 5, 0, 1, 1)
        self.gridLayoutStats = QtWidgets.QGridLayout()
        self.gridLayoutStats.setObjectName("gridLayoutStats")
        self.labelAtk = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAtk.setObjectName("labelAtk")
        self.gridLayoutStats.addWidget(self.labelAtk, 1, 0, 1, 1)
        self.labelDefEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelDefEV.setObjectName("labelDefEV")
        self.gridLayoutStats.addWidget(self.labelDefEV, 2, 2, 1, 1)
        self.labelSpAIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpAIV.setObjectName("labelSpAIV")
        self.gridLayoutStats.addWidget(self.labelSpAIV, 3, 1, 1, 1)
        self.labelSpA = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpA.setObjectName("labelSpA")
        self.gridLayoutStats.addWidget(self.labelSpA, 3, 0, 1, 1)
        self.labelDefIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelDefIV.setObjectName("labelDefIV")
        self.gridLayoutStats.addWidget(self.labelDefIV, 2, 1, 1, 1)
        self.labelHP = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHP.setObjectName("labelHP")
        self.gridLayoutStats.addWidget(self.labelHP, 0, 0, 1, 1)
        self.labelSpAEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpAEV.setObjectName("labelSpAEV")
        self.gridLayoutStats.addWidget(self.labelSpAEV, 3, 2, 1, 1)
        self.labelSpD = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpD.setObjectName("labelSpD")
        self.gridLayoutStats.addWidget(self.labelSpD, 4, 0, 1, 1)
        self.labelHPIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHPIV.setObjectName("labelHPIV")
        self.gridLayoutStats.addWidget(self.labelHPIV, 0, 1, 1, 1)
        self.labelHPEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelHPEV.setObjectName("labelHPEV")
        self.gridLayoutStats.addWidget(self.labelHPEV, 0, 2, 1, 1)
        self.labelAtkEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAtkEV.setObjectName("labelAtkEV")
        self.gridLayoutStats.addWidget(self.labelAtkEV, 1, 2, 1, 1)
        self.labelDef = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelDef.setObjectName("labelDef")
        self.gridLayoutStats.addWidget(self.labelDef, 2, 0, 1, 1)
        self.labelAtkIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelAtkIV.setObjectName("labelAtkIV")
        self.gridLayoutStats.addWidget(self.labelAtkIV, 1, 1, 1, 1)
        self.labelSpDIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpDIV.setObjectName("labelSpDIV")
        self.gridLayoutStats.addWidget(self.labelSpDIV, 4, 1, 1, 1)
        self.labelSpeEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpeEV.setObjectName("labelSpeEV")
        self.gridLayoutStats.addWidget(self.labelSpeEV, 5, 2, 1, 1)
        self.labelSpeIV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpeIV.setObjectName("labelSpeIV")
        self.gridLayoutStats.addWidget(self.labelSpeIV, 5, 1, 1, 1)
        self.labelSpDEV = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpDEV.setObjectName("labelSpDEV")
        self.gridLayoutStats.addWidget(self.labelSpDEV, 4, 2, 1, 1)
        self.labelSpe = QtWidgets.QLabel(self.groupBoxPokemon)
        self.labelSpe.setObjectName("labelSpe")
        self.gridLayoutStats.addWidget(self.labelSpe, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayoutStats, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBoxPokemon, 0, 0, 1, 1)

        self.retranslateUi(PokemonDisplay)
        QtCore.QMetaObject.connectSlotsByName(PokemonDisplay)

    def retranslateUi(self, PokemonDisplay):
        PokemonDisplay.setWindowTitle(QtWidgets.QApplication.translate("PokemonDisplay", "Pokemon", None, -1))
        self.groupBoxPokemon.setTitle(QtWidgets.QApplication.translate("PokemonDisplay", "Pokemon", None, -1))
        self.labelSpecies.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Species:", None, -1))
        self.labelSpeciesValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelGender.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Gender:", None, -1))
        self.labelGenderValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelNature.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Nature:", None, -1))
        self.labelNatureValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Hardy", None, -1))
        self.labelAbility.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Ability:", None, -1))
        self.labelAbilityValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelItem.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Item:", None, -1))
        self.labelItemValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelSV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "PSV/TSV:", None, -1))
        self.labelSVValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "0000/0000", None, -1))
        self.labelHiddenPower.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Hidden Power:", None, -1))
        self.labelHiddenPowerValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Fighting", None, -1))
        self.labelFriendship.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Friendship:", None, -1))
        self.labelFriendshipValue.setText(QtWidgets.QApplication.translate("PokemonDisplay", "0", None, -1))
        self.pushButtonUpdate.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Update", None, -1))
        self.labelMove1.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Move 1:", None, -1))
        self.labelMove1Name.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelMove1PP.setText(QtWidgets.QApplication.translate("PokemonDisplay", "PP: 0", None, -1))
        self.labelMove2.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Move 2:", None, -1))
        self.labelMove2Name.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelMove2PP.setText(QtWidgets.QApplication.translate("PokemonDisplay", "PP: 0", None, -1))
        self.labelMove3.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Move 3:", None, -1))
        self.labelMove3Name.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelMove3PP.setText(QtWidgets.QApplication.translate("PokemonDisplay", "PP: 0", None, -1))
        self.labelMove4.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Move 4:", None, -1))
        self.labelMove4Name.setText(QtWidgets.QApplication.translate("PokemonDisplay", "None", None, -1))
        self.labelMove4PP.setText(QtWidgets.QApplication.translate("PokemonDisplay", "PP: 0", None, -1))
        self.labelAtk.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Atk: 0", None, -1))
        self.labelDefEV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "EV: 0", None, -1))
        self.labelSpAIV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "IV: 0", None, -1))
        self.labelSpA.setText(QtWidgets.QApplication.translate("PokemonDisplay", "SpA: 0", None, -1))
        self.labelDefIV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "IV: 0", None, -1))
        self.labelHP.setText(QtWidgets.QApplication.translate("PokemonDisplay", "HP: 0/0", None, -1))
        self.labelSpAEV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "EV: 0", None, -1))
        self.labelSpD.setText(QtWidgets.QApplication.translate("PokemonDisplay", "SpD: 0", None, -1))
        self.labelHPIV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "IV: 0", None, -1))
        self.labelHPEV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "EV: 0", None, -1))
        self.labelAtkEV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "EV: 0", None, -1))
        self.labelDef.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Def: 0", None, -1))
        self.labelAtkIV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "IV: 0", None, -1))
        self.labelSpDIV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "IV: 0", None, -1))
        self.labelSpeEV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "EV: 0", None, -1))
        self.labelSpeIV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "IV: 0", None, -1))
        self.labelSpDEV.setText(QtWidgets.QApplication.translate("PokemonDisplay", "EV: 0", None, -1))
        self.labelSpe.setText(QtWidgets.QApplication.translate("PokemonDisplay", "Spe: 0", None, -1))

