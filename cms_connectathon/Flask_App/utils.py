# validate by writing to ig examples file and then as separate step running the IG Build:
def write_val(my_file, timestamp = None):
    from pathlib import Path
    # out_path = Path(r'\\ERICS-AIR-2\ehaas\Documents\FHIR\Davinci-Notifications\Flask_App\test_output') # test
    out_path = Path(r"\\ERICS-AIR-2\ehaas\Documents\FHIR\Davinci-Notifications\source\examples") # notification local build
    #save as IG examples
    p = out_path / f'val_message_bundle_{timestamp}.json'
    p.write_text(my_file)
    #app.logger.info(f'******writing file = val_message_bundle_{timestamp}.json to {out_path}***')
    print(f'******writing file = val_message_bundle_{timestamp}.json to {out_path}***')
