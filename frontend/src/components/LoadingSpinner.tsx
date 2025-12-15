import { cn } from "@/lib/utils";

interface LoadingSpinnerProps {
  className?: string;
  size?: "sm" | "md" | "lg";
}

export function LoadingSpinner({ className, size = "md" }: LoadingSpinnerProps) {
  const sizeClasses = {
    sm: "w-4 h-4 border-2",
    md: "w-5 h-5 border-2",
    lg: "w-6 h-6 border-[3px]",
  };

  return (
    <div
      className={cn(
        "rounded-full border-primary-foreground/30 border-t-primary-foreground animate-spin-slow",
        sizeClasses[size],
        className
      )}
    />
  );
}
