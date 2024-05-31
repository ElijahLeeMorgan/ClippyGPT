import time
import sys
import google.generativeai as palm

# Based off of https://ai.google.dev/palm_docs/text_quickstart
# ASCII Art https://ascii-generator.site/

palm.configure(api_key='')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
input = "Hello! Who are you, and what do you do?"

if len(sys.argv) != 0:
    input = sys.argv[1]

prompt = f"You are an expert Microsoft Office assistant named Clippy. Solve the following problem: {input}? Please do not include any newline characters, and answer in full sentences. Think about it and include your thought process."

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.75,
    # The maximum length of the response
    max_output_tokens=100,
)

start_time = time.time()
animation = [
			"▐⠂       ▌",
			"▐⠈       ▌",
			"▐ ⠂      ▌",
			"▐ ⠠      ▌",
			"▐  ⡀     ▌",
			"▐  ⠠     ▌",
			"▐   ⠂    ▌",
			"▐   ⠈    ▌",
			"▐    ⠂   ▌",
			"▐    ⠠   ▌",
			"▐     ⡀  ▌",
			"▐     ⠠  ▌",
			"▐      ⠂ ▌",
			"▐      ⠈ ▌",
			"▐       ⠂▌",
			"▐       ⠠▌",
			"▐       ⡀▌",
			"▐      ⠠ ▌",
			"▐      ⠂ ▌",
			"▐     ⠈  ▌",
			"▐     ⠂  ▌",
			"▐    ⠠   ▌",
			"▐    ⡀   ▌",
			"▐   ⠠    ▌",
			"▐   ⠂    ▌",
			"▐  ⠈     ▌",
			"▐  ⠂     ▌",
			"▐ ⠠      ▌",
			"▐ ⡀      ▌",
			"▐⠠       ▌"
		]

while time.time() < start_time + 5:
    for i in animation:
        time.sleep(0.1)
        sys.stdout.write(f"\r{i}")
        sys.stdout.flush()
sys.stdout.flush()
output = completion.result.strip()
output = output.ljust(587, ' ')
sys.stdout.write(f"""\r
                   .:=++==:                                                                         
                 .-+**++*#%#+.             ....................................................     
               .:+=.       =%#:          ...                                                   .:   
               :+-          -@#.         :   {output[0:48]}  ..  
          :+#%@@@#+         :@#:         :   {output[48:97]}  ..  
        -*=:..-#--=         +##.         :   {output[97:146]}  ..  
       ..    :-+            @@@@@*=      :   {output[146:195]}  ..  
               .::         .==- .:+%-    :   {output[195:244]}  ..  
         +%@@@#- .=.        ......  ==   :   {output[244:293]}  ..  
     :  .@@@@@@@:.-=       .-=-.  :: .   :   {output[293:342]}  ..  
      -. :*#%%*-.-+.  .   +@@@@@#  --    :   {output[342:391]}  ..  
       :------===-    .:  -@@@@@@. -+    :   {output[391:440]}  ..  
           .#@%        .-:..-==-.:=+.    :   {output[440:489]}  ..  
            *@#           +#*====-:      :   {output[489:538]}  ..  
            #@# .=.       +@@:    -.     :   {output[538:587]}  ..  
            #@% *@*       *@@.   %@*     :                                                      ..  
            *@% *@+       +@@   *@%      .........................      .........................   
            *%% +@+       +@%  :#@-                            .:   ....                            
            =%#.=%+       =@#  +#@                           .......                                
            -%*:-%+       -@#  **%                         ......                                   
            :@+::%+       .@#  +*%                       ::..                                       
             @+- %*:       %#. -#%                     .:                                           
             #*- =%=.     :+*  :%#:                                                                 
             =%-. *%=.   .-+-  .@#=                                                                 
              @=:  -*#+++*+:    @%+                                                                 
              *#-     ...       @%+                                                                 
              .@+:             .@%=                                                                 
               -%:.            :##.                                                                 
                +#-.           =*=                                                                  
                 =%+:.       .-==                                                                   
                  .*%*=-:::-=+=.                                                                    
                     :====--.                                                                       

""")