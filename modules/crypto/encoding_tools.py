import base64
import codecs

def run_crypto_tool(args):
    text = args.text
    mode = args.mode
    action = args.action

    print(f"[*] {action.capitalize()} '{text}' using {mode}")
    
    try:
        if action == "encode":
            if mode == "base64":
                result = base64.b64encode(text.encode()).decode()
            elif mode == "hex":
                result = text.encode().hex()
            elif mode == "rot13":
                result = codecs.encode(text, 'rot_13')
                
        elif action == "decode":
            if mode == "base64":
                result = base64.b64decode(text).decode()
            elif mode == "hex":
                result = bytes.fromhex(text).decode()
            elif mode == "rot13":
                result = codecs.decode(text, 'rot_13')
                
        print(f"[+] Result: {result}")
        
    except Exception as e:
        print(f"[-] Error during {action}: {e}")
