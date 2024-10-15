#include <stdio.h>
#include <sapi.h>
#include <sphelper.h>

#pragma comment(lib, "sapi.lib")

void speak(const char *text)
{
    ISpVoice *pVoice = NULL;

    // Initialize COM
    if (FAILED(CoInitialize(NULL)))
    {
        printf("Failed to initialize COM\n");
        return;
    }

    // Create SAPI voice instance
    if (FAILED(CoCreateInstance(&CLSID_SpVoice, NULL, CLSCTX_ALL, &IID_ISpVoice, (void **)&pVoice)))
    {
        printf("Error creating SAPI voice\n");
        CoUninitialize();
        return;
    }

    // Speak the text
    pVoice->lpVtbl->Speak(pVoice, text, SPF_IS_XML, NULL);

    // Release the voice
    pVoice->lpVtbl->Release(pVoice);

    // Uninitialize COM
    CoUninitialize();
}

int main()
{
    const char *text = "Hello, how are you today?";
    speak(text);
    return 0;
}
