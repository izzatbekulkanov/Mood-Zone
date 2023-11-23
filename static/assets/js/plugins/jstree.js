
    $('#frmt').jstree({
        'core' : {
            'data' : [
                {
                    "text" : "assets",
                    "state" : { "opened" : true },
                      "children" : [
                        {
                            "text" : "vendor",
                            "state" : { "selected" : true },
                            "default" : {
                                "icon" : "fa fa-folder text-warning"
                            },
                        },
                        { "text" : "images", "state" : { "selected" : true }, "icon" : "jstree-folder", "children" : [
                            {
                                "text" : "vendor",
                                "state" : { "selected" : true },
                                "icon" : "jstree-folder",
                            },
                            { "text" : "images", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                            { "text" : "scss", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                            { "text" : "modules", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                            { "text" : "js", "state" : { "selected" : true }, "icon" : "jstree-folder",  }
    
                        ] },
                        { "text" : "scss", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                        { "text" : "modules", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                        { "text" : "js", "state" : { "selected" : true }, "icon" : "jstree-folder",  }
    
                    ]
                    
                },
                {
                    "text" : "templates",
                    "state" : { "opened" : true },
                    "children" : [
                        {
                            "text" : "components",
                            "state" : { "selected" : true },
                            "icon" : "jstree-folder"
                        },
                        { "text" : "layouts", "state" : { "selected" : true }, "icon" : "jstree-folder", },
                        { "text" : "modules", "state" : { "selected" : true }, "icon" : "jstree-folder", },
                        { "text" : "layouts", "state" : { "selected" : true }, "icon" : "jstree-folder", },
                        { "text" : "pages", "state" : { "selected" : true }, "icon" : "jstree-folder", 
                        "children" : [
                            {
                                "text" : "dashboard",
                                "state" : { "selected" : true },
                                "icon" : "jstree-folder",
                            },
                            { "text" : "index.hbs", "state" : { "selected" : true }, "icon" : "jstree-file",  },
    
                        ]},
                    ]
                    
                },
            ]
        }
    });
    
    
    $('#frmtx').jstree({
        'core' : {
            'data' : [
                {
                    "text" : "assets",
                    "state" : { "opened" : true },
                      "children" : [
                        {
                            "text" : "vendor",
                            "state" : { "selected" : true },
                            "icon" : "jstree-folder",
                        },
                        { "text" : "images", "state" : { "selected" : true }, "icon" : "jstree-folder", "children" : [
                            {
                                "text" : "vendor",
                                "state" : { "selected" : true },
                                "icon" : "jstree-folder",
                            },
                            { "text" : "images", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                            { "text" : "scss", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                            { "text" : "modules", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                            { "text" : "js", "state" : { "selected" : true }, "icon" : "jstree-folder",  }
    
                        ] },
                        { "text" : "scss", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                        { "text" : "modules", "state" : { "selected" : true }, "icon" : "jstree-folder",  },
                        { "text" : "js", "state" : { "selected" : true }, "icon" : "jstree-folder",  }
    
                    ]
                    
                },
                {
                    "text" : "templates",
                    "state" : { "opened" : true },
                    "children" : [
                        {
                            "text" : "components",
                            "state" : { "selected" : true },
                            "icon" : "jstree-folder"
                        },
                        { "text" : "layouts", "state" : { "selected" : true }, "icon" : "jstree-folder", },
                        { "text" : "modules", "state" : { "selected" : true }, "icon" : "jstree-folder", },
                        { "text" : "layouts", "state" : { "selected" : true }, "icon" : "jstree-folder", },
                        { "text" : "pages", "state" : { "selected" : true }, "icon" : "jstree-folder", 
                        "children" : [
                            {
                                "text" : "dashboard",
                                "state" : { "selected" : true },
                                "icon" : "jstree-folder",
                            },
                            { "text" : "index.hbs", "state" : { "selected" : true }, "icon" : "jstree-file",  },
    
                        ]},
                    ]
                    
                },
            ]
        },
        'checkbox': {
            three_state: true,
            cascade: 'up'
        },
        'plugins': ["checkbox"]
    });