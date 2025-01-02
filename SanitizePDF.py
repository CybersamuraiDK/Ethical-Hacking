#!/usr/bin/env python3
#A POC of a python script that searches through the PDF, not text but PDF object, to find malicious code and replace/overwrite it rendering it safe.

import pikepdf

def sanitize_pdf(input_file, output_file):
    try:
        with pikepdf.open(input_file) as pdf:
            for obj_number, obj in enumerate(pdf.objects):
                try:
                    # Remove JavaScript or embedded files
                    if "/JS" in obj or "/JavaScript" in obj:
                        print(f"JavaScript code found in object {obj_number} and removed.")
                        del obj["/JS"]

                    if "/EmbeddedFile" in obj:
                        print(f"Embedded file found in object {obj_number} and removed.")
                        del obj["/EmbeddedFile"]

                    if "/FileAttachment" in obj:
                        print(f"File attachment found in object {obj_number} and removed.")
                        del obj["/FileAttachment"]

                    # Handle streams
                    if isinstance(obj, pikepdf.Stream):
                        try:
                            stream_data = obj.read_bytes()
                            if any(keyword in stream_data.decode(errors="ignore") for keyword in ["shell", "cmd", "powershell", "bash", "exec"]):
                                print(f"Suspicious stream detected in object {obj_number} and cleared.")
                                obj.set_stream(b"")
                        except pikepdf.PdfError as e:
                            print(f"Unfilterable stream detected in object {obj_number}. Forcing replacement.")
                            pdf.objects[obj_number] = pikepdf.Stream(pdf, data=b"Sanitized content.")

                except KeyError:
                    print(f"Object {obj_number} does not have removable keys.")
                except Exception as e:
                    print(f"Error processing object {obj_number}: {e}")

            # Save the sanitized PDF
            pdf.save(output_file)

        print(f"Sanitization complete. Clean PDF saved as '{output_file}'.")

    except Exception as e:
        print(f"Error sanitizing PDF: {e}")

# Replace with your input and output file paths
input_pdf = "test_unclean.pdf"
output_pdf = "sanitized_oscp2023_clean.pdf"

sanitize_pdf(input_pdf, output_pdf)
