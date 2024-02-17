#include <windows.h>

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch(msg) {
        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);
            TextOut(hdc, 10, 10, "Hello, World!", 13);
            EndPaint(hwnd, &ps);
        }
        break;
        default:
            return DefWindowProc(hwnd, msg, wParam, lParam);
    }
    return 0;
}

void main() {
    const char *CLASS_NAME = "SimpleWindowClass";
    WNDCLASS wc = {0};
    wc.lpfnWndProc = WndProc;
    wc.hInstance = GetModuleHandle(NULL);
    wc.lpszClassName = CLASS_NAME;
    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(0, CLASS_NAME, "Simple Window", WS_OVERLAPPEDWINDOW, 
                               CW_USEDEFAULT, CW_USEDEFAULT, 800, 600, NULL, NULL, wc.hInstance, NULL);
    if (hwnd == NULL) {
        return;
    }

    ShowWindow(hwnd, SW_SHOWDEFAULT);

    MSG msg = {0};
    while(GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
}
