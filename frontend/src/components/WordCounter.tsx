import { cn } from "@/lib/utils";

interface WordCounterProps {
  count: number;
  limit: number;
}

export function WordCounter({ count, limit }: WordCounterProps) {
  const isOverLimit = count > limit;
  const isNearLimit = count >= limit * 0.8 && count <= limit;
  
  return (
    <div className="space-y-1">
      <div className="flex items-center justify-between text-sm">
        <span className={cn(
          "font-medium transition-colors duration-200",
          isOverLimit && "text-destructive",
          isNearLimit && "text-warning",
          !isOverLimit && !isNearLimit && "text-muted-foreground"
        )}>
          {count} / {limit} kata
        </span>
        {isOverLimit && (
          <span className="text-destructive text-xs animate-fade-in">
            Melebihi batas versi gratis
          </span>
        )}
      </div>
      <p className="text-xs text-muted-foreground">Batas gratis per request</p>
    </div>
  );
}
