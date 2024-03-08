import { clsx } from "clsx/lite";
import React from "react";

export default function Loader({
  className,
}: {
  className?: React.ComponentProps<"div">["className"];
}) {
  return (
    <div
      className={clsx(
        "size-16 animate-spin rounded-full border-8 border-slate-50 border-t-transparent",
        className,
      )}
    >
      <div className="sr-only">Loader</div>
    </div>
  );
}
