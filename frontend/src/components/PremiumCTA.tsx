import { Button } from "@/components/ui/button";
import { Sparkles } from "lucide-react";

export function PremiumCTA() {
  return (
    <div className="surface-elevated rounded-xl p-5 border border-border/50 animate-fade-in">
      <div className="flex items-start gap-3">
        <div className="p-2 rounded-lg bg-accent/10">
          <Sparkles className="w-5 h-5 text-accent" />
        </div>
        <div className="flex-1 min-w-0">
          <h3 className="font-heading font-semibold text-foreground mb-1">
            Butuh hasil lebih formal?
          </h3>
          <p className="text-sm text-muted-foreground leading-relaxed mb-3">
            Mode Dosen Killer cocok untuk teks panjang dan revisi akhir sebelum bimbingan.
          </p>
          <Button variant="premium" size="sm" className="gap-2">
            <Sparkles className="w-4 h-4" />
            Upgrade / Donasi
          </Button>
        </div>
      </div>
    </div>
  );
}
