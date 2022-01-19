{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMainWindow',
          'title':u'Card Explorer v1.0',
          'size':(499, 293),
          'statusBar':1,
          'foregroundColor':(107, 255, 134),
          'backgroundColor':(84, 84, 84),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileNew',
                   'label':'&New\tCtrl+N',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileOpen',
                   'label':'&Open\tCtrl+O',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSave',
                   'label':'&Save\tCtrl+S',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSaveAs',
                   'label':'Save &As...',
                  },
                  {'type':'MenuItem',
                   'name':'fileSep1',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFilePageSetup',
                   'label':'Page Set&up...',
                  },
                  {'type':'MenuItem',
                   'name':'menuFilePrint',
                   'label':'&Print...\tCtrl+P',
                  },
                  {'type':'MenuItem',
                   'name':'menuFilePrintPreview',
                   'label':'Print Pre&view',
                  },
                  {'type':'MenuItem',
                   'name':'fileSep2',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'Edit',
             'label':'&Edit',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuEditUndo',
                   'label':'&Undo\tCtrl+Z',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditRedo',
                   'label':'&Redo\tCtrl+Y',
                  },
                  {'type':'MenuItem',
                   'name':'editSep1',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditCut',
                   'label':'Cu&t\tCtrl+X',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditCopy',
                   'label':'&Copy\tCtrl+C',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditPaste',
                   'label':'&Paste\tCtrl+V',
                  },
                  {'type':'MenuItem',
                   'name':'editSep2',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditClear',
                   'label':'Cle&ar\tDel',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditSelectAll',
                   'label':'Select A&ll\tCtrl+A',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':'&Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpAbout',
                   'label':'&About ...',
                   'command':'doHelpAbout',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'TextField', 
    'name':'txtCheckSumOk', 
    'position':(184, 170), 
    'backgroundColor':(0, 82, 5, 255), 
    'foregroundColor':(0, 255, 9, 255), 
    },

{'type':'TextField', 
    'name':'txtCheckSum', 
    'position':(11, 170), 
    'size':(154, -1), 
    'backgroundColor':(0, 79, 6, 255), 
    'foregroundColor':(0, 255, 14, 255), 
    },

{'type':'StaticText', 
    'name':'lblChecksum', 
    'position':(10, 145), 
    'backgroundColor':(84, 84, 84, 255), 
    'foregroundColor':(107, 255, 134, 255), 
    'text':u'Check Sum:', 
    },

{'type':'TextField', 
    'name':'txtReaderDetails', 
    'position':(10, 112), 
    'size':(477, -1), 
    'backgroundColor':(0, 88, 6, 255), 
    'foregroundColor':(0, 255, 17, 255), 
    },

{'type':'StaticText', 
    'name':'lblReader', 
    'position':(10, 89), 
    'backgroundColor':(84, 84, 84, 255), 
    'foregroundColor':(107, 255, 134, 255), 
    'text':u'Reader:', 
    },

{'type':'StaticText', 
    'name':'lblATR', 
    'position':(10, 40), 
    'backgroundColor':(84, 84, 84, 255), 
    'foregroundColor':(107, 255, 134, 255), 
    'text':u'ATR:', 
    },

{'type':'TextField', 
    'name':'txtCardATR', 
    'position':(10, 58), 
    'size':(477, -1), 
    'backgroundColor':(0, 90, 5, 255), 
    'foregroundColor':(0, 255, 18, 255), 
    },

{'type':'StaticText', 
    'name':'lblAppTitle', 
    'position':(11, 9), 
    'backgroundColor':(84, 84, 84, 255), 
    'font':{'style': 'bold', 'faceName': u'Sans', 'family': 'sansSerif', 'size': 14}, 
    'foregroundColor':(0, 255, 10, 255), 
    'text':u'Card Explorer', 
    },

{'type':'Button', 
    'name':'cmdReadCard', 
    'position':(400, 200), 
    'backgroundColor':(72, 72, 72, 255), 
    'foregroundColor':(1, 255, 0, 255), 
    'label':u'Read Card', 
    },

] # end components
} # end background
] # end backgrounds
} }
