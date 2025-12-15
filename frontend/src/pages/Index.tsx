import { useState, useCallback } from "react";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { WordCounter } from "@/components/WordCounter";
import { LoadingSpinner } from "@/components/LoadingSpinner";
import { PremiumCTA } from "@/components/PremiumCTA";
import { GraduationCap, ArrowRight, Copy, Check } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const WORD_LIMIT = 150;
const API_URL = "http://127.0.0.1:8000/api/humanize";

function countWords(text: string): number {
  return text.trim().split(/\s+/).filter(Boolean).length;
}

const Index = () => {
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");
  const [isProcessing, setIsProcessing] = useState(false);
  const [isCopied, setIsCopied] = useState(false);
  const { toast } = useToast();

  const wordCount = countWords(inputText);
  const isOverLimit = wordCount > WORD_LIMIT;

  const handleSubmit = useCallback(async () => {
    if (!inputText.trim()) {
      toast({
        title: "Teks kosong",
        description: "Silakan masukkan teks yang ingin diubah.",
        variant: "destructive",
      });
      return;
    }

    if (isOverLimit) {
      toast({
        title: "Teks terlalu panjang",
        description: `Versi gratis maksimal ${WORD_LIMIT} kata.`,
        variant: "destructive",
      });
      return;
    }

    setIsProcessing(true);
    setOutputText("");

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: inputText }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Terjadi kesalahan server.");
      }

      setOutputText(data.result);

      toast({
        title: "Berhasil",
        description: "Teks berhasil dirapikan ke bahasa akademik.",
      });
    } catch (error: any) {
      toast({
        title: "Terjadi kesalahan",
        description: error.message || "Gagal memproses teks.",
        variant: "destructive",
      });
    } finally {
      setIsProcessing(false);
    }
  }, [inputText, isOverLimit, toast]);

  const handleCopy = useCallback(async () => {
    if (!outputText) return;

    try {
      await navigator.clipboard.writeText(outputText);
      setIsCopied(true);
      toast({
        title: "Tersalin",
        description: "Teks berhasil disalin ke clipboard.",
      });
      setTimeout(() => setIsCopied(false), 2000);
    } catch {
      toast({
        title: "Gagal menyalin",
        description: "Tidak dapat menyalin teks.",
        variant: "destructive",
      });
    }
  }, [outputText, toast]);

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border/50 bg-card/50 backdrop-blur-sm sticky top-0 z-10">
        <div className="container py-4 md:py-5">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-primary/10">
              <GraduationCap className="w-6 h-6 text-primary" />
            </div>
            <div>
              <h1 className="font-heading text-xl md:text-2xl font-bold text-foreground">
                kating.AI
              </h1>
              <p className="text-sm text-muted-foreground hidden sm:block">
                Ubah teks mentah menjadi bahasa skripsi yang formal dan natural.
              </p>
            </div>
          </div>
        </div>
      </header>

      {/* Main */}
      <main className="container py-6 md:py-10">
        <p className="text-sm text-muted-foreground mb-6 sm:hidden text-center">
          Ubah teks mentah menjadi bahasa skripsi yang formal dan natural.
        </p>

        <div className="grid lg:grid-cols-2 gap-6 lg:gap-8">
          {/* Input */}
          <div className="space-y-3">
            <label className="text-sm font-medium text-foreground">
              Teks Asli
            </label>
            <Textarea
              variant="academic"
              placeholder="Tempelkan teks kamu di sini (draft skripsi, hasil ChatGPT, dll)"
              className="min-h-[260px] resize-none"
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              disabled={isProcessing}
            />
            <WordCounter count={wordCount} limit={WORD_LIMIT} />
          </div>

          {/* Output */}
          <div className="space-y-3">
            <div className="flex justify-between items-center">
              <label className="text-sm font-medium text-foreground">
                Versi Bahasa Akademik
              </label>
              {outputText && (
                <Button variant="ghost" size="sm" onClick={handleCopy}>
                  {isCopied ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
                </Button>
              )}
            </div>
            <Textarea
              variant="readonly"
              placeholder="Hasil perbaikan bahasa akademik akan muncul di sini."
              className="min-h-[260px] resize-none"
              value={outputText}
              readOnly
            />
          </div>
        </div>

        {/* Action */}
        <div className="mt-8 flex flex-col items-center gap-4">
          <Button
            variant="academic"
            size="lg"
            onClick={handleSubmit}
            disabled={isProcessing}
          >
            {isProcessing ? (
              <>
                <LoadingSpinner size="sm" />
                Kating lagi bantuin ngerapihin…
              </>
            ) : (
              <>
                Rapikan Jadi Bahasa Skripsi
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </Button>

          <p className="text-sm text-muted-foreground">
            Mode Gratis · Maksimal {WORD_LIMIT} kata · Tanpa login
          </p>
        </div>

        <div className="mt-10 max-w-md mx-auto">
          <PremiumCTA />
        </div>
      </main>
    </div>
  );
};

export default Index;
