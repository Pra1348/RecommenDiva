using System;
using System.Diagnostics;
using System.IO;
using System.Text.Json;

public class RecommendationService
{
    public string GetRecommendations(string inputData)
    {
        var psi = new ProcessStartInfo
        {
            FileName = "python",
            ArgumentList = { "Services/TensorFlowService.py", inputData },
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true
        };

        var process = Process.Start(psi);
        var output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();

        return output;
    }
}
