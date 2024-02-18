from phBot import *
import QtBind

pName = 'xClientlessChecker'
pVersion = '1.0.0'
pUrl = 'https://raw.githubusercontent.com/meobeo113/xClientlessChecker/main/xClientlessChecker.py'

gui = QtBind.init(__name__, 'xClientlessChecker')

QtBind.createLabel(gui, 'Welcome to the GUI example Python script! From here you\'ll be able to add your own GUI to the \'Plugins\' tab inside phBot. Being able to create a UI\nopens up far more possibilies.\n\n- Do not replace the __name__ var in the QtBind.init() call. It is used for passing events to the correct module.\n- Only call QtBind.init() during module load\n- Labels are auto resized after text is set', 10, 10)

#button1 = QtBind.createButton(gui, 'button_clicked', 'Button', 10, 125)
checkbox1 = QtBind.createCheckBox(gui, 'checkbox_clicked', 'Enable Auto Relog', 10, 150)
#label1 = QtBind.createLabel(gui, 'Label', 10, 175)
#lineedit1 = QtBind.createLineEdit(gui, 'Text in box', 10, 200, 32, 16)

QtBind.createLabel(gui, 'The only downside is that you must create the UI by hand.', 10, 250)

#def button_clicked():
#    log('Button clicked')

def checkbox_clicked(checked):
    log('Check Box: %s' % checked)

# Check Clientless
def IsClientless():
    pid = get_client()['pid']
    if pid:
        return False
    return True

log('[%s] Loaded' % __name__)