db.Song.update( {name:'singer3'}, 
				 { 
					$push: { albums: 10 } 
				 } )

db.Song.update( {name:'singer4'}, 
				 { 
					$addToSet: { albums: {$each: [100,101,102,103,104,105,106,107,108,109,110]} } 
				 }
                )

db.Song.update( {name:'singer4'}, 
				 { 
					$pull: { albums: 105 } 
				 }
                )
